from cart.views import cart_add, cart_detail, cart_remove
from django.urls import path

app_name = 'cart'
urlpatterns = [
    path('',view=cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',view=cart_add,name='cart_add'),
    path('remove/<int:product_id>/',view=cart_remove,name='cart_remove'),
]
