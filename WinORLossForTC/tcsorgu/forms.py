from django import forms

class TcAramaForm(forms.Form):
    tc_num = forms.CharField(label='TC Kimlik Numarası', max_length=11)
