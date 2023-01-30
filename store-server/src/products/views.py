from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from products.models import Product, ProductCategory, Basket
from users.models import User
from django.core.paginator import Paginator


def index(request):
    return render(request, 'products/index.html')


def products(request, category_id=None, page_number=1):

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Store - Каталог',
        'categories': (ProductCategory.objects
                                    .annotate(product_count=Count('product__id'))
                                    .filter(product_count__gt=0)
                                    .values('id', 'name')),
        'products': products_paginator,
        }
    return render(request, 'products/products.html', context=context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
