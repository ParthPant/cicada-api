from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CustomUser

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'phone_number', 'password',)

    def clean_password(self):
        return self.initial['password']


class CustomUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'email', 'is_admin', 'phone_number',)
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('name', 'email', 'password', 'phone_number',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
            (None, {
                    'classes': ('wide',),
                    'fields': ('name', 'email', 'phone_number', 'password1', 'password2',),
                   }
            ),
    )

    search_fields = ('name',)
    ordering = ('name',)

    filter_horizontal = ()

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
