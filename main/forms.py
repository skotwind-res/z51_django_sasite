from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='rubric name', max_length=100)
    age = forms.IntegerField(min_value=0, max_value=99)
