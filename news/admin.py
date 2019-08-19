from django.contrib import admin

from news.models import Article


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("header", "created")
    ordering = ("-created",)


admin.site.register(Article, ArticlesAdmin)
