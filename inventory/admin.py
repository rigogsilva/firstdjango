from django.contrib import admin


from .models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ['tittle', 'amount']

admin.site.register(Item, ItemAdmin)
