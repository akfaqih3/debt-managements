from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='Home'),
    path('accounts/',views.accounts,name='accounts'),
    path('transactions/<str:id>',views.transactions,name='transactions'),
    path('account/<str:id>',views.account,name='account'),
    path('updateTransaction/',views.updateTransaction,name='updateTransaction'),
    path('deleteTransaction/',views.deleteTransaction,name='deleteTransaction'),
    path('updateAccount/',views.updateAccount,name='updateAccount'),
    path('deleteAccount/',views.deleteAccount,name='deleteAccount'),
]