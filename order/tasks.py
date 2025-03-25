from io import BytesIO
from celery import shared_task
from django.contrib.staticfiles import finders
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
import weasyprint

from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order.id}'
    message = (
        f'Dear {order.first_name},\n\n'
        f'You have successfully placed an order.'
        f'Your order ID is {order.id}.'
    )
    mail_sent = send_mail(
        subject, message, 'admin@myshop.com', [order.email]
    )
    return mail_sent


@shared_task
def payment_completed(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'My shop - Invoice no. {order.id}'
    message  = (
        "Please find the attached Invoice for you recent purchase."
    ) 
    email = EmailMessage(
        subject,message,'admin@admin.com',[order.email]
    )
    html = render_to_string('orders/order/pdf.html',{'order':order})
    out = BytesIO()

    stylesheets = [weasyprint.CSS(finders.find('css/pdf.css'))]
    weasyprint.HTML(string=html).write_pdf(out,stylesheets = stylesheets)
    email.attach(f'order_{order_id}.pdf',out.getvalue(),'application/pdf')
    email.send()

