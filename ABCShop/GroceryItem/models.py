


from django.db import models
from django.core import validators

# Create your models here.
GRYTYPE = [ ['oil', 'Oil'], ['grain', 'Grain'], ['cosmetic', 'Cosmetic'] ]

class GroceryItem(models.Model):
    name = models.CharField(max_length = 5)
    typ =  models.CharField(max_length = 8, choices = GRYTYPE)
    quantity = models.PositiveSmallIntegerField()
    rpu = models.PositiveSmallIntegerField(validators = [validators.MinValueValidator(10), validators.MaxValueValidator(500)])
    amount = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.name + '-' + self.typ + '-' + str(self.quantity) + '-' + str(self.rpu) + '-' +str(self.amount)

    class Meta:
        ordering = ('quantity','name')
