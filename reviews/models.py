from django.db.models import Model, TextField, CharField, DateTimeField
from django.utils.translation import ugettext_lazy as _


class Review(Model):
    class Meta:
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    text = TextField(_("text"))
    author = CharField(_("author"), max_length=128)
    created = DateTimeField(_("creation date"), auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.created.strftime('%d-%m-%Y')}"
