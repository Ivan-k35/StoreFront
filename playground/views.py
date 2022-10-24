from django.shortcuts import render
from store.models import Product, OrderItem


def say_hello(request):
    queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('-title')

    return render(request, 'playground/hello.html', {'name': 'Ivan', 'products': list(queryset)})
