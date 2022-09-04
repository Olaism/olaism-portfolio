from django import forms

class ContactForm(forms.Form):
    your_email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(label="Your Message", max_length=4000, widget=forms.Textarea)