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
    filtered =Transaction.objects.filter( account=id)
    withdraw =sum(item.balance for item in filtered.filter(type='سحب') )
    deposit =sum(item.balance for item in filtered.filter(type='إصال') )
    context = {'Account':Account.objects.get(id=id),'withdraw':withdraw , 'deposit':deposit,'remaining':int(withdraw)-int(deposit), 'transactions':Transaction.objects.filter(account=id)}
    return render(request,'transactions.html',context)