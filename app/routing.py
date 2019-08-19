from channels.routing import ProtocolTypeRouter

from news.consumer import NewsConsumer

application = ProtocolTypeRouter(
    {
        # Empty for now (http->django views is added by default)
        "websocket": NewsConsumer
    }
)
