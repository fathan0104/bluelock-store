import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from main.models import Product
from main.forms import ProductForm

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

# CREATE (create_product → create_product) 
@login_required(login_url='/login')
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, "Product successfully added!")
            return redirect('main:show_main')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)


# DETAIL (product_detail → product_detail)
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
    product_list = Product.objects.filter(user=request.user)
    data = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return HttpResponse(serializers.serialize("json", product_list), content_type="application/json")

def show_xml_by_id(request, product_id):
    product_item = Product.objects.filter(pk=product_id)
    if product_item.exists():
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail if product.thumbnail else None,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login') # Sukses, kembali
    
    else:
        form = UserCreationForm() # Form kosong untuk request GET

    context = {'form': form}
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
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {
    'form': form
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) 
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user
    price = request.POST.get("price") 
    stock = request.POST.get("stock")

    new_product = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
        price = price,
        stock = stock
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Login status successful.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login successful!"
                # Add other data if you want to send data to Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password."
        }, status=401)
        
@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "status": True,
            "message": "Logout berhasil!",
            "username": username,
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout gagal."
        }, status=401)            
        
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        user.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)