from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django import forms


class User(User):
    def __str__(self):
        return self.get_full_name()


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
