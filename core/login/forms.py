from datetime import datetime

from django import forms
from django.contrib.auth import authenticate

from core.security.choices import LOGIN_ATTEMPT
from core.user.models import User
from core.security.models import UserAccess


class AuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un username',
        'class': 'form-control',
        'autocomplete': 'off'
    }), label='Usuario')

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese un password',
        'class': 'form-control',
        'autocomplete': 'off'
    }), label='Contraseña')

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get('username', '')
        password = cleaned.get('password', '')
        if len(username) == 0:
            raise forms.ValidationError('Ingrese su username')
        elif len(password) == 0:
            raise forms.ValidationError('Ingrese su password')
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            user = queryset[0]
            if not user.is_active:
                raise forms.ValidationError('El usuario ha sido bloqueado. Comuníquese con su administrador.')
            if authenticate(username=username, password=password) is None:
                UserAccess(user=user, login_attempt=LOGIN_ATTEMPT[1][0]).save()
                intent = user.useraccess_set.filter(login_attempt=LOGIN_ATTEMPT[1][0], date_joined=datetime.now().date()).count()
                if intent > 2:
                    user.is_active = False
                    user.save()
                    raise forms.ValidationError('El usuario ha sido bloqueado por superar el límite de intentos fallidos en un día.')
                count = 3 - intent
                raise forms.ValidationError(f"La contraseña ingresada es incorrecta, por favor intentelo de nuevo. Le quedan {count} {'intento' if count == 1 else 'intentos'}. Si supera los 3 intentos fallidos su cuenta sera bloqueada.")
            UserAccess(user=user).save()
            return cleaned
        raise forms.ValidationError('Por favor introduzca el nombre de usuario y la clave correctos para una cuenta de personal. Observe que ambos campos pueden ser sensibles a mayúsculas.')

    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)


class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un username',
        'class': 'form-control',
        'autocomplete': 'off'
    }), label='Usuario')

    def clean(self):
        cleaned = super().clean()
        users = User.objects.filter(username=cleaned['username'])
        if not users.exists():
            raise forms.ValidationError('El usuario que ingreso no existe en el sistema')
        return cleaned

    def get_user(self):
        return User.objects.get(username=self.cleaned_data.get('username'))


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese un password',
        'class': 'form-control',
        'autocomplete': 'off'
    }), label='Password')

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita el password',
        'class': 'form-control',
        'autocomplete': 'off'
    }), label='Confirmación de password')

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirm_password = cleaned['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas deben ser iguales')
        return cleaned
