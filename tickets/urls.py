from django.urls import path
from .views import decode_pnr

urlpatterns = [
    path('decode_pnr/', decode_pnr, name='decode_pnr'),
]