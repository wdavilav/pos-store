import json
import time

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, TemplateView

from core.pos.forms import CategoryForm
from core.pos.models import Category
from core.security.mixins import GroupPermissionMixin

MODULE_NAME = 'Categorías'


class CategoryListView(GroupPermissionMixin, TemplateView):
    template_name = 'category/list.html'
    permission_required = 'view_category'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'search':
                data = []
                for i in Category.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['list_url'] = reverse_lazy('category_list')
        context['create_url'] = reverse_lazy('category_create')
        context['module_name'] = MODULE_NAME
        print(self.request.user_agent)
        return context


class CategoryCreateView(GroupPermissionMixin, CreateView):
    template_name = 'category/create.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'add_category'

    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST['action']
        try:
            if action == 'add':
                data = self.get_form().save()
            else:
                data['error'] = 'No ha seleccionado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nuevo registro de una Categoría'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['module_name'] = MODULE_NAME
        return context


class CategoryUpdateView(GroupPermissionMixin, UpdateView):
    template_name = 'category/create.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'change_category'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

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
        context['title'] = 'Edición de una Categoría'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['module_name'] = MODULE_NAME
        return context


class CategoryDeleteView(GroupPermissionMixin, DeleteView):
    model = Category
    template_name = 'delete.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'delete_category'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.get_object().delete()
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Categoría'
        context['list_url'] = self.success_url
        context['module_name'] = MODULE_NAME
        return context
