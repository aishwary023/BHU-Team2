from django.urls import path
from .views import StockView

urlpatterns=[
    path('stock/create/', StockView.as_view()),
]