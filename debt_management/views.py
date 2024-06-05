from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Account,Transaction
from datetime import date
# Create your views here.

def index(request):
    context={
        'Transactions':Transaction.objects.all(),
        'Accounts':Account.objects.all(),
        'accountChose':Account.objects.filter(active=True)
    }
    return render(request,'index.html',context)

def transactions(request,id):
    filtered =Transaction.objects.filter( account=id)
    withdraw =sum(item.balance for item in filtered.filter(type='سحب') )
    deposit =sum(item.balance for item in filtered.filter(type='سداد') )
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

def updateTransaction(request):
    id = request.POST.get('pk')
    updateTransaction = Transaction.objects.get(pk=id)
    updateTransaction.type = request.POST.get('type')
    updateTransaction.account = Account.objects.get(name=request.POST.get('account'))
    updateTransaction.balance = request.POST.get('balance')
    updateTransaction.content = request.POST.get('content')
    updateTransaction.date = request.POST.get('transaction_date')

    updateTransaction.save()

    return HttpResponseRedirect(reverse('Home'))

def deleteTransaction(request):
    delete_id = request.POST.get('delete_id')
    Transaction.objects.get(pk=delete_id).delete()

    return HttpResponseRedirect(reverse('Home'))

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

def updateAccount(request):
    id = request.POST.get('pk')
    updateAccount = Account.objects.get(pk=id)
    updateAccount.name= request.POST.get('name')
    updateAccount.phone= request.POST.get('phone')
    updateAccount.allow_max= request.POST.get('allow_max')
    updateAccount.type = request.POST.get('type')
    updateAccount.active = request.POST.get('active')=='on'
    updateAccount.save()

    return HttpResponseRedirect(reverse('accounts',args=str(id)))

def deleteAccount(request):
    delete_id = request.POST.get('delete_account_id')
    Account.objects.get(pk=delete_id).delete()

    return HttpResponseRedirect(reverse('Home'))