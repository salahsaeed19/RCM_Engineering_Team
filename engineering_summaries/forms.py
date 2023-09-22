from django import forms
from .models import EngineeringSummary

class EngineeringSummaryForm(forms.ModelForm):
    class Meta:
        model = EngineeringSummary
        fields = ['title', 'content', 'category', 'source_link', 'image']
