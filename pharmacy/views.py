from django.shortcuts import render, redirect
from .models import Item, Check
from datetime import datetime,date
from pyzbar import pyzbar
from PIL import Image
import base64

# Create your views here.
def items(request):
    items = Item.objects.all()
    return render(request, 'pharmacy/home.html',{'items': items})

def codeReader(request):
    return render(request, 'pharmacy/reader.html')

def codeCheck(request):
    if request.method == 'POST':
        firstimg = str(request.POST.get('img64'))
        print(firstimg)
        img = base64.b64decode(firstimg)
        info = pyzbar.decode(Image.open(img))
        return render(request, 'pharmacy/check.html', {'img': info})

def addItem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        amount = request.POST.get('amount')
        code = request.POST.get('code')

        newDrug = Item(name=name,price=price,code=code,pub_date=datetime.now(),amount=amount)
        newDrug.save()
        return redirect('home')


def form(request):
    return render(request, 'pharmacy/form.html')

def compare(request):
    if request.method == 'POST':
        code = request.POST.get('code');
        item = Item.objects.get(code=code);
        return render(request, 'pharmacy/found.html', {'item': item})

def wsitems(request):
    check = Check(price=0,pub_date=datetime.now())
    check.save()
    return render(request, 'pharmacy/homews.html', {'checkid': check.id})