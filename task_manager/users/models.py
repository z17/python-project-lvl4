from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label=_('First Name')
    )
    last_name = forms.CharField(
        required=True,
        label=_("Second Name")
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name')
