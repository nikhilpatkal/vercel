import asyncio
import time
from django.http import HttpResponse
from django.shortcuts import render

from portfolio_app.models import backend_lang, card, core_lang, front_lang, lets_cofee

# Create your views here.

def homepage(req):
    card_sec=card.objects.all()
    core = core_lang.objects.all()
    front = front_lang.objects.all()
    back = backend_lang.objects.all()
    data= {'card_sec':card_sec,'core': core,'front':front,'back':back}
    return render(req,"home.html",data)

def cofee_data(req):
    print("hello")
    asyncio.sleep(3)
    cofee_name = req.POST.get('name')
    cofee_email = req.POST.get('email')
    cofee_text=req.POST.get('text')

    new_post = lets_cofee(
       name=cofee_name,
       email=cofee_email,
       text=cofee_text
        
    )
    new_post.save()
    return HttpResponse("<h1>Thanku</h1>")
def next_page(req):
    return HttpResponse("<h1>Hello I am Nikhil Patkal</h1>")