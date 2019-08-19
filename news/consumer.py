import json
from typing import List

from channels.generic.websocket import JsonWebsocketConsumer

from news.exceptions import ClientError
from news.models import Article


class NewsConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive_json(self, content, **kwargs):
        content = json.loads(content)
        action = content["action"]
        payload = content.get("payload", {})

        try:
            try:
                if action == "last":
                    count = payload.get("count", 10)
                    content = self.get_latest_articles(count)

                elif action == "all":
                    content = self.get_all_articles()

                elif action == "previous":
                    start = payload["start"]
                    count = payload.get("count", 10)
                    content = self.get_previous(start, count)

                else:
                    raise ClientError(message="invalid action")

                self.send_json(content)

            except (KeyError, AttributeError, AssertionError) as e:
                raise ClientError(message="invalid content")

        except ClientError as e:
            self.send_json({"error": e.message})

    def get_latest_articles(self, count: int):
        assert type(count) == int

        articles = Article.objects.order_by("-created")[:count]
        return {"articles": self._serialize(articles)}

    def get_all_articles(self):
        articles = Article.objects.order_by("-created")
        return {"articles": self._serialize(articles)}

    def get_previous(self, start: int, count: int):
        assert type(start) == int
        assert type(count) == int

        articles = Article.objects.filter(id__lt=start).order_by("-created")[:count]
        return {"articles": self._serialize(articles)}

    @staticmethod
    def _serialize(articles: List[Article]):
        return [
            {
                "id": article.id,
                "header": article.header,
                "text": article.text,
                "picture": article.picture.url,
            }
            for article in articles
        ]
