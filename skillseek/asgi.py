# skillseek/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import core.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillseek.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            skillseek.routing.websocket_urlpatterns
        )
    ),
})