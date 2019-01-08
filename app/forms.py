
from django import forms
from .models import Contract_LCR

class Contract_LCR_Form(forms.ModelForm):
    class Meta:
        model = Contract_LCR
        fields = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',)