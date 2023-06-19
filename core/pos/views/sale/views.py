import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, FormView

from core.pos.forms import *
from core.pos.utilities import printer
from core.reports.forms import ReportForm
from core.security.mixins import GroupPermissionMixin

MODULE_NAME = 'Ventas'


class SaleListView(GroupPermissionMixin, FormView):
    template_name = 'sale/admin/list.html'
    form_class = ReportForm
    permission_required = 'view_sale'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                start_date = request.POST['start_date']
                end_date = request.POST['end_date']
                queryset = Sale.objects.filter()
                if len(start_date) and len(end_date):
                    queryset = queryset.filter(date_joined__range=[start_date, end_date])
                for i in queryset.order_by('-id'):
                    data.append(i.toJSON())
            elif action == 'search_detail_products':
                data = []
                for i in SaleDetail.objects.filter(sale_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['list_url'] = reverse_lazy('sale_admin_list')
        context['create_url'] = reverse_lazy('sale_admin_create')
        context['module_name'] = MODULE_NAME
        return context


class SaleCreateView(GroupPermissionMixin, CreateView):
    model = Sale
    template_name = 'sale/admin/create.html'
    form_class = SaleForm
    success_url = reverse_lazy('sale_admin_list')
    permission_required = 'add_sale'

    def post(self, request, *args, **kwargs):
        action = request.POST['action']
        data = {}
        try:
            if action == 'add':
                with transaction.atomic():
                    company = Company.objects.first()
                    iva = float(company.iva) / 100
                    sale = Sale()
                    sale.company = company
                    sale.employee_id = request.user.id
                    sale.client_id = int(request.POST['client'])
                    sale.iva = iva
                    sale.dscto = float(request.POST['dscto']) / 100
                    sale.cash = float(request.POST['cash'])
                    sale.change = float(request.POST['change'])
                    sale.save()
                    for i in json.loads(request.POST['products']):
                        product = Product.objects.get(pk=i['id'])
                        detail = SaleDetail()
                        detail.sale_id = sale.id
                        detail.product_id = product.id
                        detail.cant = int(i['cant'])
                        detail.price = float(i['pvp'])
                        detail.dscto = float(i['dscto']) / 100
                        detail.save()
                        sale.calculate_detail()
                        detail.product.stock -= detail.cant
                        detail.product.save()
                    sale.calculate_invoice()
                    data = {'print_url': str(reverse_lazy('sale_admin_print_invoice', kwargs={'pk': sale.id}))}
            elif action == 'search_products':
                ids = json.loads(request.POST['ids'])
                data = []
                term = request.POST['term']
                queryset = Product.objects.filter(Q(stock__gt=0) | Q(is_service=True)).exclude(id__in=ids).order_by('name')
                if len(term):
                    queryset = queryset.filter(Q(name__icontains=term) | Q(code__icontains=term))
                    queryset = queryset[:10]
                for i in queryset:
                    item = i.toJSON()
                    item['pvp'] = float(i.pvp)
                    item['value'] = i.get_full_name()
                    item['dscto'] = '0.00'
                    item['total_dscto'] = '0.00'
                    data.append(item)
            elif action == 'search_client':
                data = []
                term = request.POST['term']
                for i in Client.objects.filter(Q(names__icontains=term) | Q(dni__icontains=term)).order_by('names')[0:10]:
                    data.append(i.toJSON())
            elif action == 'create_client':
                form = ClientForm(self.request.POST)
                data = form.save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_final_consumer(self):
        queryset = Client.objects.filter(dni='9999999999999')
        if queryset.exists():
            return json.dumps(queryset[0].toJSON())
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['frmClient'] = ClientForm()
        context['list_url'] = self.success_url
        context['title'] = 'Nuevo registro de una Venta'
        context['action'] = 'add'
        context['company'] = Company.objects.first()
        context['final_consumer'] = self.get_final_consumer()
        context['module_name'] = MODULE_NAME
        return context


class SaleDeleteView(GroupPermissionMixin, DeleteView):
    model = Sale
    template_name = 'delete.html'
    success_url = reverse_lazy('sale_admin_list')
    permission_required = 'delete_sale'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Venta'
        context['list_url'] = self.success_url
        context['module_name'] = MODULE_NAME
        return context


class SalePrintInvoiceView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            sale = Sale.objects.get(id=self.kwargs['pk'])
            context = {'sale': sale, 'height': 450 + sale.saledetail_set.all().count() * 10}
            pdf_file = printer.create_pdf(context=context, template_name='sale/format/ticket.html')
            return HttpResponse(pdf_file, content_type='application/pdf')
        except:
            pass
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
