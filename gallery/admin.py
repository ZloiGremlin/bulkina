# vim:fileencoding=utf-8
from gallery.models import Album, Image
from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin


class AdminInlineImage(AdminImageMixin, admin.TabularInline):
    model = Image
    extra = 10


class AlbumAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"url": ("name",)}
    search_fields = ['name']
    list_display = ['name', 'main']
    inlines = [AdminInlineImage]


admin.site.register(Album, AlbumAdmin)