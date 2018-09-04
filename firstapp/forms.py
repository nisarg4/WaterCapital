from django import forms
from django.forms import DateField, ModelForm



class UpdateDetailsForm(forms.Form):
 excel_file = forms.FileField(label='Excel File',required=False,validators=[".xlsx"])