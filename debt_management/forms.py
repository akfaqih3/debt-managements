from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Transaction,Account

account_type =(
    ('دائن','دائن'),
    ('مدين','مدين')
)

transaction_type =(
    ('سحب','سحب'),
    ('سداد','سداد'),
)

class AccountAdd(forms.ModelForm):
    name = forms.CharField(max_length=32,label='الاسم',widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=16,label='رقم الموبايل',widget=forms.TextInput(attrs={'class':'form-control'}))
    type =forms.ChoiceField(choices=account_type,label='نوع الحساب',widget=forms.Select(attrs={'class':'form-control'}))
    allow_max = forms.DecimalField(max_digits=7,label='أعلى قيمة مسموح بها',decimal_places=2,widget=forms.TextInput(attrs={'class':'form-control'}))
    active = forms.BooleanField(required=False ,label='نشط',widget=forms.CheckboxInput(attrs={'class':'form-control'}))

    class Meta:
        model=Account
        fields= ['name','phone','type','allow_max','active']


# accounts_choice = [  (value,label) for value,label in Account.objects.filter(active=True).values_list('id','name')]

class TransactionAdd(forms.ModelForm):
    type =forms.ChoiceField(choices=transaction_type,label='نوع العملية',widget=forms.Select(attrs={'class':'form-control'}))
    balance = forms.DecimalField(max_digits=7,label='المبلغ',decimal_places=2,widget=forms.TextInput(attrs={'class':'form-control'}))
    content =forms.CharField(label='البيان',widget=forms.TextInput(attrs={'class':'form-control'}))
    account = forms.Select()
    class Meta:
        model = Transaction
        fields =['type','account','balance','content']
