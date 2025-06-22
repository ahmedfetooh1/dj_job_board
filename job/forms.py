from django import forms
from .models import Apply ,JOB


class ApplyForm(forms.ModelForm):
    class Meta :
        model = Apply
        fields = ['name','email','website','cv','cover_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model = JOB
        fields = '__all__'
        exclude = 'slug',