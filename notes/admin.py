from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display =["title", "owner", "created_at", "updated_at"]
    list_filter=["created_at", "updated_at", "owner"]


admin.site.register(Note, NoteAdmin)
