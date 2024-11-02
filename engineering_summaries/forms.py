from django import forms
from .models import EngineeringSummary, EngineeringCategory

class EngineeringSummaryForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=EngineeringCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = EngineeringSummary
        fields = ['title', 'content', 'categories', 'source_link', 'image']
