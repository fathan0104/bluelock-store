from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Product
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    last_login_time = request.COOKIES.get('last_login', None) 
    
    context = {
        'npm': '2406496284',
        'name': request.user.username,
        'class' : 'PBP E',
        'product_list': products,
        'last_login': last_login_time, # Menggunakan variabel yang sudah di-check
    }
    return render(request, "main.html", context)

def add_employee(request):
    add_employee = Employee.objects.create(name = "john",age = 23, persona = "Kerja keras")
    return HttpRessponse("Employee ditambahkan")

# CREATE (create_news → create_product) 
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "create_product.html", context)

# DETAIL (news_detail → product_detail)
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()
    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

# SERIALIZER (JSON & XML)
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    product_item = Product.objects.filter(pk=product_id)
    if product_item.exists():
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    product_item = Product.objects.filter(pk=product_id)
    if product_item.exists():
        json_data = serializers.serialize("json", product_item)
        return HttpResponse(json_data, content_type="application/json")
    return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    news = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=news)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_news.html", context)

def delete_product(request, id):
    news = get_object_or_404(Product, pk=id)
    news.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
