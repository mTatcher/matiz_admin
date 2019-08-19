from django.db.models import Model, CharField, TextField, ImageField, DateTimeField
from django.utils.translation import ugettext_lazy as _


class Article(Model):
    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    header = CharField(verbose_name=_("header"), max_length=128)
    text = TextField(verbose_name=_("text"))
    picture = ImageField(verbose_name=_("image"))
    created = DateTimeField(verbose_name=_("creation date"), auto_now_add=True)

    def __str__(self):
        return self.header
