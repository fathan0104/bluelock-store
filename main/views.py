from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm

def show_main(request):
    return render(request, "main.html")

# CREATE (create_news → create_product)
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

# DETAIL (news_detail → product_detail)
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

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
