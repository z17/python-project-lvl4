from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        label=_('First Name')
    )
    last_name = forms.CharField(
        required=True,
        label=_("Second Name")
    )
    email = forms.EmailField(
        required=True,
        label=_("Email")

    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
