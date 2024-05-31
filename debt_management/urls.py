from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='Home'),
    path('transactions/<str:id>',views.transactions,name='transactions'),
    path('accounts/<str:id>',views.accounts,name='accounts'),
    path('addTransaction/',views.addTransaction,name='addTransaction'),
    path('addAccount/',views.addAccount,name='addAccount')
]