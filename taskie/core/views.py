from django.shortcuts import render
from django.views.decorators.cache import cache_page

@cache_page(60 * 10)
def mainpage(request):
    return render(request, template_name="core/index.html")
