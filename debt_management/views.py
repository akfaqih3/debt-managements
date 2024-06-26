from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .models import Account,Transaction
from datetime import date
from .forms import AccountAdd,TransactionAdd

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    if request.method == "POST":
        newTransaction = TransactionAdd(request.POST)
        if newTransaction.is_valid:
            newTransaction.save()
    context={
        'TransactionForm': TransactionAdd,
        'AccountForm':AccountAdd,
        'Transactions':Transaction.objects.all().order_by('-id')
    }
    return render(request,'index.html',context)
    
@login_required
def transactions(request,id):
    filtered =Transaction.objects.filter( account=id)
    withdraw =sum(item.balance for item in filtered.filter(type='سحب') )
    deposit =sum(item.balance for item in filtered.filter(type='سداد') )
    context = {'Account':Account.objects.get(id=id),'withdraw':withdraw , 'deposit':deposit,'remaining':int(withdraw)-int(deposit), 'transactions':filtered}
    
    return render(request,'transactions.html',context)
@login_required
def account(request,id):
    filtered = Account.objects.get(pk=id)
    context={
        'AccountForm':AccountAdd,
        'TransactionForm': TransactionAdd,
        'account':filtered}

    return render(request,'account.html',context)
@login_required
def accounts(request):
    if request.method =="POST":
        form = AccountAdd(request.POST)
        if form.is_valid():
            form = form.save()
    context = {
        'AccountForm':AccountAdd,
        'TransactionForm': TransactionAdd,
        'accounts':Account.objects.all(),
        
    }
    return render(request,'accounts.html',context=context)
@login_required
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
@login_required
def deleteTransaction(request):
    delete_id = request.POST.get('delete_id')
    Transaction.objects.get(pk=delete_id).delete()

    return HttpResponseRedirect(reverse('Home'))
@login_required
def updateAccount(request):
    id = request.POST.get('pk')
    updateAccount = Account.objects.get(pk=id)
    updateAccount.name= request.POST.get('name')
    updateAccount.phone= request.POST.get('phone')
    updateAccount.allow_max= request.POST.get('allow_max')
    updateAccount.type = request.POST.get('type')
    updateAccount.active = request.POST.get('active')=='on'
    updateAccount.save()

    return HttpResponseRedirect(reverse('accounts'))
@login_required
def deleteAccount(request):
    delete_id = request.POST.get('delete_account_id')
    Account.objects.get(pk=delete_id).delete()

    return HttpResponseRedirect(reverse('accounts'))
