from datetime import datetime

from crum import get_current_request
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.forms import model_to_dict

from config import settings
from core.security.choices import LOGIN_ATTEMPT
from core.user.models import User


class Dashboard(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')
    icon = models.CharField(max_length=500, verbose_name='Icono FontAwesome')
    image = models.ImageField(upload_to='dashboard/%Y/%m/%d', null=True, blank=True, verbose_name='Logo')
    author = models.CharField(max_length=120, verbose_name='Autor')

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return f'{settings.MEDIA_URL}{self.image}'
        return f'{settings.STATIC_URL}img/empty.png'

    class Meta:
        verbose_name = 'Dashboard'
        verbose_name_plural = 'Dashboards'
        default_permissions = ()
        permissions = (
            ('view_dashboard', 'Can view Dashboard'),
        )


class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    hour = models.TimeField(default=datetime.now)
    remote_addr = models.CharField(max_length=100, null=True, blank=True)
    login_attempt = models.CharField(max_length=20, choices=LOGIN_ATTEMPT, default=LOGIN_ATTEMPT[0][0])
    http_user_agent = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.remote_addr

    def toJSON(self):
        item = model_to_dict(self)
        item['user'] = self.user.toJSON()
        item['date_joined'] = self.date_joined.strftime('%d-%m-%Y')
        item['hour'] = self.hour.strftime('%H:%M %p')
        item['login_attempt'] = {'id': self.login_attempt, 'name': self.get_login_attempt_display()}
        return item

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            request = get_current_request()
            self.remote_addr = request.META['REMOTE_ADDR']
            self.http_user_agent = str(request.user_agent)
        except:
            pass
        super(UserAccess, self).save()

    class Meta:
        verbose_name = 'Acceso de Usuario'
        verbose_name_plural = 'Acceso de Usuarios'
        default_permissions = ()
        permissions = (
            ('view_user_access', 'Can view Acceso de Usuario'),
            ('delete_user_access', 'Can delete Acceso de Usuario'),
        )
