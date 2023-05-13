from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . models import category,product
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

def allproduct(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        products_list=product.objects.all().filter(category=c_page,available=True)

    else:
        products_list=product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page_number=request.GET.get('page','1')
    except:
        page_number=1
    try:
        products=paginator.page(page_number)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request,'category.html',{'cate':c_page,'pro':products})

def productde(request,c_slug,product_slug):
    try:
        products=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'prodet':products})