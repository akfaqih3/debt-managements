from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='Home'),
    path('transactions/<str:id>',views.transactions,name='transactions'),
    path('accounts/<str:id>',views.accounts,name='accounts'),
    path('addTransaction/',views.addTransaction,name='addTransaction'),
    path('updateTransaction/',views.updateTransaction,name='updateTransaction'),
    path('deleteTransaction/',views.deleteTransaction,name='deleteTransaction'),
    path('addAccount/',views.addAccount,name='addAccount'),
    path('updateAccount/',views.updateAccount,name='updateAccount'),
    path('deleteAccount/',views.deleteAccount,name='deleteAccount')
]