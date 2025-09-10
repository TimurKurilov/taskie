from django.shortcuts import render
from django.views.decorators.cache import cache_page

def mainpage(request):
    return render(request, template_name="core/index.html")
