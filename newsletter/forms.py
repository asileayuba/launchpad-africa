from django import forms

class NewsletterForm(forms.Form):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Your Email ID', 'class': 'email-input'})
    )
