from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CreationForm

class CreationView(CreateView):
    form_class = CreationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy("auth:login")
