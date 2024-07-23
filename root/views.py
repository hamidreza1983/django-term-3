from typing import Any
from django.shortcuts import render, redirect
from services.models import SpecialService
from .models import FrequentlyQuestions, ContactUs
from services.models import Team
from .forms import ContactUsForm
from django.contrib import messages
from django.views.generic import TemplateView


from django.http import HttpRequest, HttpResponse


# def home(request):

#     context = {
#         'specials': SpecialService.objects.filter(status=True),
#         'team' : Team.objects.filter(status=True),
#         'questions': FrequentlyQuestions.objects.filter(status=True)[::-1],
#         }
    
#     return render(request, 'root/index.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
#            name = form.cleaned_data['name']
#            email = form.cleaned_data['email']
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            new_contact = ContactUs()
#            new_contact.name = name
#            new_contact.email = email
#            new_contact.subject = subject
#            new_contact.message = message
#            new_contact.save()

            messages.add_message(request, messages.SUCCESS, 'your message was submited successfully')
            return redirect('root:contact')
        else:
            messages.add_message(request, messages.ERROR, 'your input data may be incorrect')
            return redirect('root:contact')
    else:
        form = ContactUsForm()
        return render(request, "root/contact.html", context = {'form': form})


# def about(request):
#     context = {
#         'team' : Team.objects.filter(status=True),
#         }
#     return render(request, "root/about.html", context=context)

# Create your views here.

class AboutView(TemplateView):
    template_name = "root/about.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context ['team'] = Team.objects.all()
        return context



class HomeView(TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context ['team'] = Team.objects.all()
        context ['specials'] = SpecialService.objects.filter(status=True)
        context ['questions'] = FrequentlyQuestions.objects.filter(status=True)[::-1]
        return context
