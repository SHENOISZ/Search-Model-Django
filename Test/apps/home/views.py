from django.shortcuts import render
from apps.search.engine import Engine
from .models import Home
# Create your views here.

def index(request):

    obj = []
    search = '' 

    if request.method == "POST":

        search = request.POST['q']
        print(search)
        engine = Engine()

        # camps charfield, slugfield or textfield only
        fields=['nome', 'slug','texto']

        obj = engine.search(obj=Home, fields=fields, q=search, method='post')
        #obj = engine.search(obj=Home, fields=fields, q=search, method='post', order_by='-visitas', limit=10, filter={'nome':'tokyo ghoul'})
          

    return render(request, 'home/index.html', {'obj': obj, 'search': search})