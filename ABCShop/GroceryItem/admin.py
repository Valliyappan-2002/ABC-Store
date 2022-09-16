

from django.contrib import admin
from GroceryItem import models

# Register your models here.


@admin.register(models.GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'typ', 'quantity', 'amount', 'toBeCalled') # to be displayed in change list
    exclude = ('amount',)  # to be displayed in form
    #overriding ordering in model (default ordering)
    ordering = ('name',)
    
    def toBeCalled(self, obj):
        print(self, 'type:', type(self))
        if obj.typ == 'oil':
            return '6 month'
        elif obj.typ == 'cosmetic':
            return None
        else:
            return '1 year'
    toBeCalled.short_description = 'Usable Period'

    def save_model(self, request, obj, form, change):
        obj.amount = obj.rpu * obj.quantity
        super(GroceryItemAdmin, self).save_model(request, obj, form, change)

        
    
admin.register(models.GroceryItem)
#admin.site.register(models.GroceryItem, GroceryItemAdmin)
