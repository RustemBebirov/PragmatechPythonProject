from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Order,Order_Comment
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

class OrderListView(ListView):
    model = Order
    template_name = 'shop.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()


class OrderDetailView(DetailView):
    model = Order
    template_name = 'shop-single.html'
    context_object_name = 'order'


#Cokkies
def like_order(request):
    if request.method == 'POST':
        liked_orders = request.COOKIES.get('liked_orders', '')
        order_id = request.POST.get('order_id')
    html = render_to_string('successfuly_liked.html')
    response = HttpResponse(html)
    if order_id not in liked_orders.split(','):
        response.set_cookie("liked_orders",f'{liked_orders}{order_id},')
    return response

def like_order_page(request):
    like_orders = request.COOKIES.get('liked_orders','')
    liked_order_ids=[]
    for i in like_orders:
        try:
            j=int(i)
            liked_order_ids.append(j)
        except:
            print('None')

    orders = Order.objects.filter(id__in=liked_order_ids)
    context ={
        'orders': orders
    }
    return render(request,'liked_orders.html',context)

def add_order(request):
    if request.method == 'POST':
        add_orders = request.COOKIES.get('add_orders', '')
        order_id = request.POST.get('order_id')
    html = render_to_string('successfuly_added.html')
    response = HttpResponse(html)
    if order_id not in add_orders.split(','):
        response.set_cookie("add_orders",f'{add_orders}{order_id},')
    return response

def add_order_page(request):
    add_orders = request.COOKIES.get('add_orders','')
    add_order_ids=[]
    for i in add_orders:
        try:
            j=int(i)
            add_order_ids.append(j)
        except:
            print('None')

    orders = Order.objects.filter(id__in=add_order_ids)
    context ={
        'orders': orders
    }
    return render(request,'add_orders.html',context)
#cookies end