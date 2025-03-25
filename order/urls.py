from django.urls import path

from .views import admin_order_details, order_create,admin_order_pdf
app_name = 'orders'
urlpatterns =  [
    path('create/',view=order_create,name='order_create' ),
    path('admin/order/<int:order_id>',view=admin_order_details,name='admin_order_details'),
    path('admin/order/<int:order_id>/pdf/',view=admin_order_pdf,name='admin_order_pdf'),
]
