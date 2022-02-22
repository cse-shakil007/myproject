from django.contrib import admin
from .models import Update, Blocked, File, VIP, Free, Data

class UpdateAdmin(admin.ModelAdmin):
    list_display = ['version', 'title', 'status', 'created_at', 'updated_at']
    list_filter = ['title', 'status']

class BlockedAdmin(admin.ModelAdmin):
    list_display = ['id', 'apps', 'status', 'created_at', 'updated_at']
    list_filter = ['apps', 'status']


admin.site.register(Update, UpdateAdmin)
admin.site.register(Blocked, BlockedAdmin)
admin.site.register(File)
admin.site.register(VIP)
admin.site.register(Free)
admin.site.register(Data)
