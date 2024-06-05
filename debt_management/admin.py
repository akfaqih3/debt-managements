from django.contrib import admin
from .models import Account,Transaction
# Register your models here.


class AccountDisplay(admin.ModelAdmin):
    list_display = ['name','type','phone','allow_max']
    list_filter = ['type','register_date']

class TransactionDisplay(admin.ModelAdmin):
    list_display = ['type','account','content','balance']
    list_filter = ['account','type']
    
admin.site.register(Account,AccountDisplay)
admin.site.register(Transaction,TransactionDisplay)