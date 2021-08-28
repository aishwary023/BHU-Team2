from django.urls import path
from .views import StockCreateView, StockListView

urlpatterns=[
    path('stock/create/', StockCreateView.as_view()),
    path('stock/list/', StockListView.as_view()),
]