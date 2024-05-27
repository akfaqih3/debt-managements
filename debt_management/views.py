from django.shortcuts import render
from .models import Account,Transaction
# Create your views here.

def index(request):
    context={
        'Transactions':Transaction.objects.all(),
        'Accounts':Account.objects.all()
    }
    return render(request,'index.html',context)

def transactions(request,id):
    context = {'Account':Account.objects.get(id=id), 'transactions':Transaction.objects.filter(account=id)}
    return render(request,'transactions.html',context)