from django.http import HttpResponse
from django.views import View
from django.db import connection
from django.shortcuts import render

from .models import Products

class MyView(View):
    def get(self, request, *args, **kwargs):
        all_ = Products.objects.all()
        
        for e in Products.objects.all():
            print (e.origname)
        
        print(all_)
        return render(request, "try.html", context={'x':all_})