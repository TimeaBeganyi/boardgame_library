from datetime import date

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.forms import TextInput, EmailInput, DateTimeInput, Select, DateInput, Textarea
from django import forms

from userextend.models import UserExtend, UserProfile


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'email_confirmation', 'username', 'date_of_birth', 'gender',
                  'phone_number']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email address', 'class': 'form-control'}),
            'email_confirmation': EmailInput(
                attrs={'placeholder': 'Please confirm your email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter a username', 'class': 'form-control'}),
            'date_of_birth': DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please confirm your password'

    def clean(self):
        cleaned_data = self.cleaned_data
        users = UserExtend.objects.all()
        for user in users:
            if user.email == cleaned_data.get('email'):
                msg = 'An user with this email already exists!'
                self._errors['username'] = self.error_class([msg])
        today = date.today()
        if cleaned_data.get('date_of_birth') > today:
            msg = 'Birth date cannot be in the future!'
            self.errors['date_of_birth'] = self.error_class([msg])

        return cleaned_data


class UserExtendUpdateForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'email_confirmation', 'username', 'gender', 'date_of_birth','phone_number']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email address', 'class': 'form-control'}),
            'email_confirmation': EmailInput(
                attrs={'placeholder': 'Please confirm your email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter an username', 'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': TextInput(attrs={'placeholder': 'Please enter your phone number', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        today = date.today()
        if cleaned_data.get('date_of_birth') > today:
            msg = 'Birth date cannot be in the future!'
            self.errors['date_of_birth'] = self.error_class([msg])

        return cleaned_data


class UserExtendUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['about', 'profile_image']

        widgets = {
            'about': Textarea(attrs={'placeholder': 'Please enter your bio', 'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].widget.attrs['class'] = 'form-control'


class AuthenticationLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class PasswordChangeFormExtend(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter old password'})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm new password'})


class PasswordResetFormExtend(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-contral', 'placeholder': 'Please enter your email address'})


class SetPasswordFormExtend(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm a new password'})
