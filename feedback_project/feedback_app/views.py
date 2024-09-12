from django.shortcuts import render
from django.core.mail import send_mail
from .forms import FeedbackForm

# Create your views here.
def Feedback_View(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            user_email=form.cleaned_data['emial']
            send_mail('Thank you for your feedback','trydjango.emailhost@gmail.com',[user_email],fail_silently=False)
            return ('thank_you')
        
        else:
            form = FeedbackForm()
    
        return render(request,'feedback_form.html',{'form':form})
    
def thank_you(request):
    return render(request,'thank_you.html')