from django.db import models
from datetime import date
# Create your models here.


class Account(models.Model):
    A_type=[
        ('دائن','دائن'),
        ('مدين','مدين')
        ]

    name = models.CharField(max_length=32,verbose_name='اسم الحساب')
    phone = models.CharField(max_length=16,verbose_name='رقم الموبايل',null=True,blank=True)
    allow_max = models.DecimalField(default=3000.00,max_digits=7 , decimal_places=2,verbose_name='اعلى قيمة مسموح بها')
    type= models.CharField(max_length=16, default=A_type[0],choices=A_type,verbose_name='نوع الحساب')
    #image = models.ImageField(upload_to='images/%y/%m/%d/',null=True,blank=True,verbose_name='صورة الحساب')
    register_date = models.DateField(default=date.today,verbose_name='تاريخ تسجيل الحساب')
    active = models.BooleanField(default=True,verbose_name='حالة الحساب')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='الحسابات'
        

class Transaction(models.Model):
    T_type=[
        ('سحب','سحب'),
        ('سداد','سداد')
        ]

    type = models.CharField(max_length=16,default=T_type[0],choices=T_type,verbose_name='نوع العملية')
    account = models.ForeignKey(Account,on_delete=models.PROTECT)
    balance = models.DecimalField(default=0.00,max_digits=7,decimal_places=2 ,verbose_name='المبلغ')
    content = models.TextField(null=True,blank=True,verbose_name='البيان')
    date = models.DateField(auto_now=True,verbose_name='التاريخ')

    def __str__(self):
        return f"{self.account}      {self.balance}"
    
    class Meta:
        verbose_name= 'التحويلات'