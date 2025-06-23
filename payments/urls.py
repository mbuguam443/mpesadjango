# payments/urls.py

from django.urls import path
from .views import mpesa_callback
from .views import mpesa_callback, initiate_stk_push

urlpatterns = [
    path('callback/', mpesa_callback, name='mpesa_callback'),
    path('stk/', initiate_stk_push, name='initiate_stk'),
]
