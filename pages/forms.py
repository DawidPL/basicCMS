from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Twoje imie", max_length=100, required=True)
    lastname = forms.CharField(label="Nazwisko", max_length=100, required=False)
    email = forms.EmailField(label="Adres email", max_length=100, required=True)
    tel = forms.CharField(label="numer telefonu", max_length=100, required=False)
    message = forms.CharField(label="Treść wiadomości", widget=forms.Textarea, required=True)
