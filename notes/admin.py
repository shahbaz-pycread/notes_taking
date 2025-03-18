from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "created_at"]
    search_fields = ("user",)
    
admin.site.register(Note, NoteAdmin)
