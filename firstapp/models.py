
from django.db import models
from django import forms
from django.forms import ModelForm, DateField

import firstapp
from WaterCapital import settings


class DateRangeForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'),
                                 input_formats=('%d/%m/%Y',))
    end_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'),
                               input_formats=('%d/%m/%y',),
                               required=False)


# Create your models here.
# class Transactio(models.Model):
#     value_date  = models.DateField()
#     value       = models.FloatField()
#     type        = models.TextField(max_length=254)
#     name        = models.TextField(max_length=254)

#GS Transaction Model
class GS_Tran(models.Model):
    advisor  = models.TextField(null=True)
    fund       = models.TextField(null=True)
    base_currency        = models.TextField(max_length=3,null=True)
    currency        = models.TextField(max_length=25,null=True)
    opening_balance = models.FloatField(null=True)
    forwards = models.TextField(null=True)
    product_description = models.TextField(max_length=254,null=True)
    product_id = models.TextField(max_length=254,null=True)
    tradeDate = models.TextField(null=True)
    settleDate= models.TextField(null=True)
    activity = models.TextField(null=True)
    account_type = models.IntegerField(null=True)
    tradeQuantity = models.FloatField(null=True)
    tradePrice = models.FloatField(null=True)
    commInt = models.FloatField(null=True)
    netAmt = models.FloatField(null=True)
    brokerDesc = models.TextField(null=True)
    accNo = models.IntegerField(null=True)
    ref_no = models.TextField(max_length=254,null=True)

class Tradar_Tran(models.Model):
    trade  = models.IntegerField()
    fund       = models.TextField()
    type        = models.TextField()
    amount        = models.FloatField(null=True)
    security_type = models.TextField()
    ticker = models.TextField()
    isin = models.TextField(max_length=254,null=True)
    cusip = models.TextField(max_length=254,null=True)
    sedol = models.TextField(null=True)
    description= models.TextField(null=True)
    price = models.FloatField(null=True)
    trans_date = models.TextField(null=True)
    ccy = models.TextField(null=True)
    settles = models.TextField(null=True)
    account = models.TextField(null=True)
    cashflow = models.FloatField(null=True)
    balance = models.FloatField(null=True)

class SSB_Trans(models.Model):
    fund  = models.TextField(null=True)
    ticker       = models.TextField(null=True)
    isin        = models.TextField(null=True)
    sedol        = models.TextField(null=True)
    ss_asset_id = models.TextField(null=True)
    other_id = models.TextField(null=True)
    transaction = models.TextField(max_length=254,null=True)
    transaction_id = models.TextField(max_length=254,null=True)
    transaction_no = models.TextField(null=True)
    transaction_description= models.TextField(null=True)
    cash_type = models.TextField(null=True)
    fx_type = models.TextField(null=True)
    investment_type_code = models.IntegerField(null=True)
    share_quantity = models.FloatField(null=True)
    net_amt = models.FloatField(null=True)
    actual_net_amt = models.FloatField(null=True)
    settle_loc = models.TextField(null=True)
    ss_status = models.TextField(null=True)
    ss_trans_type = models.TextField(null=True)
    time_stamp = models.TextField(null=True)
    pay_settle_date = models.TextField(null=True)
    executing_broker = models.TextField(null=True)
    currency = models.TextField(null=True)
    action_type = models.TextField(null=True)
    security_name = models.TextField(null=True)
    ss_status = models.TextField(null=True)
    ss_trade_id = models.TextField(null=True)
    trade_record_date = models.TextField(null=True)

class SSB_Balance(models.Model):
    fund  = models.TextField(null=True)
    currency = models.TextField(null=True)
    amount = models.FloatField(null=True)
    fund_internal = models.TextField(null=True)

class GS_Balance(models.Model):
    acc_no  = models.IntegerField(null=True)
    acc_name = models.TextField(null=True)
    currency = models.TextField(null=True)
    td_quantity = models.FloatField(null=True)
    sd_quantity = models.FloatField(null=True)
    business_date = models.TextField(null=True)

class Tradar_Balance(models.Model):
    field1  = models.TextField(null=True)
    field2 = models.TextField(null=True)
    field3 = models.TextField(null=True)
    trade = models.TextField(null=True)
    type = models.TextField(null=True)
    amount = models.TextField(null=True)
    security  = models.TextField(null=True)
    ticker=models.TextField(null=True)
    isin = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)
    date = models.FloatField(null=True)
    settles = models.TextField(null=True)
    cashflow = models.FloatField(null=True)
    balance = models.FloatField(null=True)