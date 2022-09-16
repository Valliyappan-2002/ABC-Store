


from GroceryItem.form import GroceryForm
from django.shortcuts import render
from django.http import HttpResponse
from GroceryItem.models import GroceryItem

# Create your views here.


def makeEntry(req):
    if req.method == 'GET':
        gi  = GroceryForm()
        return render(req, 'grocery.txt', {'form':gi})
    else:
        gf = GroceryForm(req.POST)
        if gf.is_valid():
            gi = gf.save(commit = False)
            gi.amount = int(req.POST['rpu']) * int(req.POST['quantity'])
            gi.save()
            return HttpResponse('Grocery item details has been recorded successfully and the amount is: '+str(gi.amount))
        else:
            return render(req, 'grocery.txt', {'form':gf})


def dispEntries(req):
    items = GroceryItem.objects.all()
    if len(items) > 10:
        return render(req, 'dispGryEntries.txt', {'lst':items[:10]})
    else:
        return render(req, 'dispGryEntries.txt', {'lst':items})
        
            




            
        



