from django import forms
from reports.models import Report

# class ReportForm(forms.ModelForm):
#     class Meta:
#         model = Report
#         fields = ['first_name', 'last_name', 'address', 'description']

class ReportForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'input1 lang pl',
            'placeholder': 'Imię',


        }),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'input1 lang pl',
            'placeholder': 'Nazwisko'
        }),
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'input1 lang pl',
            'placeholder': 'Ulica nr domu, Kod pocztowy, Miasto'
        }),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'input1 lang pl',
            'placeholder': 'Opis'
        }),
    )
    photo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'btn-image input1 lang pl',
        }),
    )

    class Meta:
        model = Report  # Powiązanie formularza z modelem Report
        fields = ['first_name', 'last_name', 'address', 'description', 'photo']