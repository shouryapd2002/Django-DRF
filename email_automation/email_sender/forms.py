from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    body = forms.CharField(widget=forms.Textarea)
    recipients = forms.FileField() 
    attachment = forms.FileField(required=False)