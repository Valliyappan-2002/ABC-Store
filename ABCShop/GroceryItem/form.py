

from django import forms
from GroceryItem.models import GroceryItem

class GroceryForm(forms.ModelForm):

    class Meta:
        model = GroceryItem
        exclude = ('amount',)


        
