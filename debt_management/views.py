from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Account,Transaction
from datetime import date
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
    context = {'Account':Account.objects.get(id=id),'withdraw':withdraw , 'deposit':deposit,'remaining':int(withdraw)-int(deposit), 'transactions':Transaction.objects.filter(account=id),'Accounts':Account.objects.all()}
    
    return render(request,'transactions.html',context)

def accounts(request,id):
    filtered = Account.objects.get(pk=id)
    context={'account':filtered}

    return render(request,'accounts.html',context)

def addTransaction(request):
    newTransacion= Transaction()
    newTransacion.type = request.POST.get('type') 
    newTransacion.account = Account.objects.get(name=request.POST.get('account'))
    newTransacion.balance = request.POST.get('balance') 
    newTransacion.content = request.POST.get('content')
    newTransacion.date = date.today()
    Transaction.save(newTransacion)

    return HttpResponseRedirect(reverse('transactions',args=str(newTransacion.account.pk)))

def addAccount(request):
    newAccount=Account()
    newAccount.name= request.POST.get('name')
    newAccount.phone= request.POST.get('phone')
    newAccount.allow_max= request.POST.get('allow_max')
    newAccount.type = request.POST.get('type')
    newAccount.active = request.POST.get('active')=='on'
    newAccount.register_date = date.today()
    Account.save(newAccount)

    return HttpResponseRedirect(reverse('accounts',args=str(newAccount.pk)))