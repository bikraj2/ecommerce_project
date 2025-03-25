from django.urls import path

from payment import webhooks
from payment.views import payment_completed, payment_process,payment_canceled
app_name = 'payment'
urlpatterns =  [
path ('process/',view=payment_process,name='process'),
path ('completed/',view=payment_completed,name='completed'),
path ('canceled/',view=payment_canceled,name='canceled'),
path ('webhook/',view=webhooks.stripe_webhook,name='stripe-webhook'),
]
