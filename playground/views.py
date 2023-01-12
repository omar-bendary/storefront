from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from django.core.cache import cache
import requests
from django.views.decorators.cache import cache_page


@cache_page(5*60)
def say_hello(request):

    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()

    return render(request, 'hello.html', {'name': data})
