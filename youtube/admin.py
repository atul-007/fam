from django.contrib import admin
from django.utils.html import format_html
from . import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_image', 'title', 'description']
    search_fields = ('video_id', 'channel_id', 'title', 'description')
    list_filter = ('publish_datetime',)

    def thumbnail_image(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px;" />', obj.thumbnail_url)

    thumbnail_image.allow_tags = True
    thumbnail_image.short_description = 'Thumbnail'

@admin.register(models.APIAuthKey)
class APIKeyAdmin(admin.ModelAdmin):
    fields = ['auth_key', 'exhausted']
