import json

from django.http import HttpResponse
from django.views.generic import UpdateView

from config import settings
from core.pos.forms import CompanyForm
from core.pos.models import Company
from core.security.mixins import GroupPermissionMixin

MODULE_NAME = 'Compañia'


class CompanyUpdateView(GroupPermissionMixin, UpdateView):
    template_name = 'company/create.html'
    model = Company
    form_class = CompanyForm
    success_url = settings.LOGIN_REDIRECT_URL
    permission_required = 'view_company'

    def get_object(self, queryset=None):
        queryset = Company.objects.filter()
        if queryset.exists():
            return queryset[0]
        return Company()

    def get_form(self, form_class=None):
        form = super(CompanyUpdateView, self).get_form(form_class)
        instance = self.get_object()
        if instance.pk is not None:
            form.instance = instance
        return form

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'edit':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de la compañia'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['module_name'] = MODULE_NAME
        return context
