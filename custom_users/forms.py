# myapp/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

# from users.models import MembershipStatus


class CustomUserEditForm(UserEditForm):
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))

    # Use ModelForm's automatic form fields generation for the model's `country` field,
    # but use an explicit custom form field for `status`.
    class Meta(UserEditForm.Meta):
        fields = UserEditForm.Meta.fields | {"country"}


class CustomUserCreationForm(UserCreationForm):
    # status = forms.ModelChoiceField(queryset=MembershipStatus.objects, required=True, label=_("Status"))

    # Use ModelForm's automatic form fields generation for the model's `country` field,
    # but use an explicit custom form field for `status`.
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields | {"country"}
