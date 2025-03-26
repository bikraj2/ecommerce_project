from django.urls import path

from payment import webhooks
from payment.views import payment_completed, payment_process,payment_canceled
from django.utils.translation import gettext_lazy as _
app_name = 'payment'
urlpatterns =  [
path (_('process/'),view=payment_process,name='process'),
path (_('completed/'),view=payment_completed,name='completed'),
path (_('canceled/'),view=payment_canceled,name='canceled'),
path ('webhook/',view=webhooks.stripe_webhook,name='stripe-webhook'),
]
