import json

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, FormView

from core.reports.forms import ReportForm
from core.security.mixins import GroupPermissionMixin
from core.security.models import UserAccess

MODULE_NAME = 'Accesos de Usuarios'


class UserAccessListView(GroupPermissionMixin, FormView):
    template_name = 'user_access/list.html'
    form_class = ReportForm
    permission_required = 'view_user_access'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                queryset = UserAccess.objects.filter()
                start_date = request.POST['start_date']
                end_date = request.POST['end_date']
                if len(start_date) and len(end_date):
                    queryset = queryset.filter(date_joined__range=[start_date, end_date])
                for i in queryset:
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Accesos de los usuarios'
        context['module_name'] = MODULE_NAME
        return context


class UserAccessDeleteView(GroupPermissionMixin, DeleteView):
    model = UserAccess
    template_name = 'delete.html'
    success_url = reverse_lazy('user_access_list')
    permission_required = 'delete_user_access'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Acceso de Usuario'
        context['list_url'] = self.success_url
        context['module_name'] = MODULE_NAME
        return context
