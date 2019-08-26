from django.contrib import admin

from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "created")
    ordering = ("-created",)


admin.site.register(Review, ReviewAdmin)
