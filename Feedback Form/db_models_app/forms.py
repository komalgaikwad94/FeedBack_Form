from django import forms
from .models import ContactQuery,FeedbackForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactQuery
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'query': forms.Textarea(attrs={'class': 'form-control'}),
        }
class FeedbackForms (forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
