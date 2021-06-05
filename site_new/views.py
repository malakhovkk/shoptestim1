from django.http import HttpResponse
from django.views import View
from django.db import connection
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ProductsForm

from .models import Products
import django_tables2 as tables
from .table_test import SimpleTable

class MyView(View):
    def get(self, request, *args, **kwargs):

        all_ = Products.objects.all()
        
        for e in Products.objects.all():
            print (e.origname)
        
        print(all_)
        return render(request, "try.html", context={'x':all_})

    def post(self, request):
        #Products.object.create(origname="1", code="1", uid="1")
        form = ProductsForm(request.POST)
        form.save()
        all_ = Products.objects.all()
        return render(request, "try.html", context={'x':all_})



class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Products.objects.all()
    template_name = "simple_list.html"
