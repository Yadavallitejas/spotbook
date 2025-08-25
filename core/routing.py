# skillseek/routing.py
from django.urls import re_path
from core import consumers

# skillseek/routing.py
websocket_urlpatterns = [
    re_path(r'ws/bookings/$', consumers.BookingConsumer.as_asgi()),
    re_path(r'ws/chat/(?P<booking_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]