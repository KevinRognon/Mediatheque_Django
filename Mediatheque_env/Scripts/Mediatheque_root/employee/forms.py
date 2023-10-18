from django import forms

class MemberForm(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
