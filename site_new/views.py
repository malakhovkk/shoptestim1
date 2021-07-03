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

        #all_ = Products.objects.all()
        all_ = Products.objects.raw('SELECT S.origname as origname, F.origname as category, S.id AS id, S.uid as uid, S.code as code FROM products AS F INNER JOIN products AS S ON F.Uid=S.Parent_uid  ')
        for e in Products.objects.all():
            print (e.origname)

        categories = set(Products.objects.raw('SELECT  F.origname as category, S.id as id FROM products AS F INNER JOIN products AS S ON F.Uid=S.Parent_uid  '))
        inf = []
        for i in categories:
            inf.append(i.category)
        print(inf)
        set_categories = set(inf)
        res = []
        for cat in set_categories:
            names = []
            for el in all_:
                if cat == el.category:
                    #res.append({'category':el.category,'content':{'origname':el.origname,'id': el.id, 'uid': el.uid, 'code': el.code} })
                    names.append(el.origname)
            res.append({'category':cat, 'names': names})
        print(res)
        return render(request, "try.html", context={'x':res})

    def post(self, request):
        #Products.object.create(origname="1", code="1", uid="1")
        form = ProductsForm(request.POST)
        form.save()
        all_ = Products.objects.all()
        # category:wine
        # content:['1','2',...]
        #
        #
        return render(request, "try.html", context={'x':all_})



class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Products.objects.all()
    template_name = "simple_list.html"
