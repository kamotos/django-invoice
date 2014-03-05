from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from addressbook.models import Address
from invoice.models import Invoice

User = get_user_model()


def get_profile(user):
    return user if hasattr(settings, 'AUTH_USER_MODEL') else user.get_profile()


class InvoiceAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            address = args[0]['address']
        except IndexError:
            address = None

        try:
            user = args[0]['user']
            if not address and user:
                address_pk = get_profile(User.objects.get(pk=user)).address.pk
                args[0]['address'] = address_pk
        except (IndexError, ObjectDoesNotExist):
            pass

        super(InvoiceAdminForm, self).__init__(*args, **kwargs)

        try:
            user = int(args[0]['user'])
            addresses = get_profile(User.objects.get(pk=user)).addresses
        except ObjectDoesNotExist:
            addresses = Address.objects.none()
        except (IndexError, ValueError):
            try:
                addresses = get_profile(kwargs['instance'].user).addresses
            except (KeyError, ObjectDoesNotExist):
                addresses = Address.objects.none()
        self.fields['address'].queryset = addresses

    class Meta:
        model = Invoice
