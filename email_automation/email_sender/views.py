from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import EmailForm
from .tasks import send_bulk_emails

def email_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipients = form.cleaned_data['recipients']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            attachment = form.cleaned_data['attachment']
            
            send_bulk_emails.delay(subject, body, recipients, attachment)
            return render(request, 'email_sender/success.html')
    else:
        form = EmailForm()
    return render(request, 'email_from.html', {'form': form})