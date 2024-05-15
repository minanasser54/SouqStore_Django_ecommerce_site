from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from.models import Product

# Create your views here.


def product_list(request):
    products=Product.objects.all()
    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context={'products':products}
    return render(request,'Product/product_list.html',context)

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    context={'product':product}
    return render(request,'Product/product_detail.html',context)
