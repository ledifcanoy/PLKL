from django.db.models import fields
from django.forms import ModelForm
from .models import CustomerInformation

class cusinfo(ModelForm):
    class Meta:
        model= CustomerInformation
        fields = ['itemname', 'itememail', 'itemmobile', 'itempayment', 'itemwallet']
