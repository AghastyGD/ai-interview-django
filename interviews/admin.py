from django.contrib import admin
from .models import Chat, Message

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("title", "job", "completed")