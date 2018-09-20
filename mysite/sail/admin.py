from django.contrib import admin
from sail.models import Book, Impression

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Impression)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page')
    list_display_links = ('id', 'name')


admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')
    list_display_links = ('id', 'comment')


admin.site.register(Impression, ImpressionAdmin)
