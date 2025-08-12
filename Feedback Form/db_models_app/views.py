from django.shortcuts import render, redirect
from .forms import *
from .models import  *

def home_view(request):
    return render(request, 'feedback_app/home.html')

def about_view(request):
    return render(request, 'feedback_app/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'feedback_app/contact.html', {
                'form': ContactForm(),
                'message': 'Query submitted successfully!',
                'show_button': True
            })
    else:
        form = ContactForm()
    return render(request, 'feedback_app/contact.html', {'form': form})


def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/db/feedback/list/')
        else:
            form = FeedbackForms()
            return render(request, 'feedback_app/feedback_form.html', {'form': form})
    else:
        form = FeedbackForms()
        return render(request, 'feedback_app/feedback_form.html',{'form':form})


def feedback_list_view(request):
    return render(request, 'feedback_app/feedback_list.html', {
        'feedbacks': FeedbackForm.objects.all()
    })

def contact_queries_list_view(request):
    return render(request, 'feedback_app/contact_queries_list.html', {
        'queries': ContactQuery.objects.all()
    })
