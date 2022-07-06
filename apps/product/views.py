import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import AddToCartForm
from .models import Category, Product, ProductStatusEnum

from apps.cart.cart import Cart
def veiwProducts(request):
    product = Product.objects.all()
    # print(product)
    paginator = Paginator(product,20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products.html',{'page_obj':page_obj,'product':paginator,'pages':pages})


def veiwProductsSoon(request):
    product = Product.objects.filter(product_status = ProductStatusEnum.SOON)
    # print(product)
    paginator = Paginator(product,20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products_soon.html',{'page_obj':page_obj,'product':paginator,'pages':pages})


def veiwProductsAvailable(request):
    product = Product.objects.filter(product_status = ProductStatusEnum.AVAILABLE)
    # print(product)
    paginator = Paginator(product,20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products_available.html',{'page_obj':page_obj,'product':paginator,'pages':pages})


def veiwProductsStock(request):
    product = Product.objects.filter(product_status = ProductStatusEnum.OUTOFSTOCK)
    # print(product)
    paginator = Paginator(product,20)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
        pages = paginator.page(page_number)
    except:
        page_obj = paginator.get_page(1)
        pages = paginator.page(1)
    return render(request,'product/view_products_stock.html',{'page_obj':page_obj,'product':paginator,'pages':pages})

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})

def product(request, category_slug, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    paginator = Paginator(product,25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    context = {
        'form': form,
        'product': product,
        'similar_products': similar_products,
        # 'imagesstring': "[" + imagesstring.rstrip(',') + "]"
        'page_obj': page_obj,
    }

    return render(request, 'product/product.html', context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})