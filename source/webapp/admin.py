from django.contrib import admin
from webapp.models import Publication, Comment


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
