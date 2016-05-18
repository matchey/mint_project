from django import forms
from django.forms import ModelForm

from .models import Kansuu


class TourokuForm(forms.Form):
    func_name = forms.CharField(max_length=200)
    program_name = forms.CharField(max_length=200)
    explanation = forms.CharField(max_length=200, widget=forms.Textarea)

    class Meta:
        model = Kansuu

    def __str__(self):
        return self.func_name


# class TourokuForm(ModelForm):
#     func_name = forms.CharField()
#     program_name = forms.CharField()
#     explanation = forms.CharField(widget=forms.Textarea)
#
#     class Meta:
#         model = Kansuu
#
#     def __str__(self):
#         return self.func_name
