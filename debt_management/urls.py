from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='Home'),
    path('transactions/<str:id>',views.transactions,name='transactions')
]