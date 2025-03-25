from django.urls import path
from .views import product_detail, product_list
app_name = 'shop'
urlpatterns = [
    path('',view=product_list,name='product_list'),
    path('<slug:category_slug>/',view=product_list,name='product_list_by_category'),
    path('<int:product_id>/<slug:slug>',view=product_detail,name='product_detail')
]
