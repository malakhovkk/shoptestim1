import django_tables2 as tables
from .models import Products

class SimpleTable(tables.Table):
    class Meta:
        model = Products
        