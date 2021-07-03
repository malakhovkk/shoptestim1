from django.urls import path
from .views import ProductsView
app_name = "api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('products/', ProductsView.as_view()),
]