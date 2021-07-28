from django.urls import path
from .views import OrderDetailView,OrderListView,like_order,like_order_page,add_order,add_order_page

app_name = 'orders'

urlpatterns = [
    path('shop/', OrderListView.as_view(), name='shop'),
    path('shop-single/<int:pk>', OrderDetailView.as_view(), name='shop-single'),
    path('like/',like_order,name='like_order'),
    path('add/',add_order,name='add_order'),
    path('liked-order/',like_order_page,name='like_orders'),
    path('add-order/',add_order_page,name='add_orders'),
]
