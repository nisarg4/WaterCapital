from django.db import connection
from django.shortcuts import render_to_response, render
from django.http import HttpResponseBadRequest, HttpResponse
from django import forms
from firstapp.models import GS_Tran,Tradar_Tran,SSB_Trans,SSB_Balance,GS_Balance,Tradar_Balance

class UploadFileForm(forms.Form):
    file = forms.FileField()


def clear_records(request):
    return render(request,"clear_records.html")



def import_sheet(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
               # name_columns_by_row=2,
                model=GS_Tran,
                mapdict=['advisor','fund', 'base_currency', 'currency','opening_balance','forwards', 'product_description', 'product_id','tradeDate','settleDate', 'activity', 'account_type','tradeQuantity','tradePrice', 'commInt', 'netAmt','brokerDesc','accNo','ref_no'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'index.html',
        {'form': form})

def tradar(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
               # name_columns_by_row=2,
                model=Tradar_Tran,
                mapdict=['trade','fund', 'type', 'amount','security_type','ticker', 'isin', 'cusip','sedol','description', 'price', 'trans_date','ccy', 'settles', 'account','cashflow','balance'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_tradar.html',
        {'form': form})



def ssb_transaction(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
               # name_columns_by_row=2,
                model=SSB_Trans,
                mapdict=['fund','ticker', 'isin', 'sedol','ss_asset_id','other_id', 'transaction', 'transaction_id','transaction_no','transaction_description', 'cash_type', 'fx_type','investment_type_code', 'share_quantity', 'net_amt','actual_net_amt','settle_loc','ss_status', 'ss_trans_type', 'time_stamp','pay_settle_date','executing_broker', 'currency','action_type','security_name','ss_status', 'ss_trade_id','trade_record_date'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_ssb.html',
        {'form': form})


def ssb_balance(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
               # name_columns_by_row=2,
                model=SSB_Balance,
                mapdict=['fund','currency','amount','fund_internal'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_ssb_balance.html',
        {'form': form})



def gs_balance(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
               # name_columns_by_row=2,
                model=GS_Balance,
                mapdict=['acc_no','acc_name','currency','td_quantity','sd_quantity','business_date'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_gs_balance.html',
        {'form': form})

def tradar_balance(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            request.FILES['file'].save_to_database(
               # name_columns_by_row=2,
                model=Tradar_Balance,
                mapdict=['field1','field2','field3','trade','type','amount','security','ticker','isin','description','price','date','settles','cashflow','balance'])
            return HttpResponse("OK")
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'upload_tradar_balance.html',
        {'form': form})



def drop_tradar_tran(request):

    cursor = connection.cursor()

    cursor.execute(
        '''truncate table firstapp_tradar_tran''')
    row = cursor.fetchall()

    context = {
        "row": row
    }
    return render(request, "drop_table.html", context)

def drop_tradar_balance(request):

    cursor = connection.cursor()

    cursor.execute(
        '''truncate table firstapp_tradar_balance''')
    row = cursor.fetchall()

    context = {
        "row": row
    }
    return render(request, "drop_table.html", context)

def drop_gs_balance(request):

    cursor = connection.cursor()

    cursor.execute(
        '''truncate table firstapp_gs_balance''')
    row = cursor.fetchall()

    context = {
        "row": row
    }
    return render(request, "drop_table.html", context)

def drop_gs_tran(request):

    cursor = connection.cursor()

    cursor.execute(
        '''truncate table firstapp_gs_tran''')
    row = cursor.fetchall()

    context = {
        "row": row
    }
    return render(request, "drop_table.html", context)

def drop_ssb_trans(request):

    cursor = connection.cursor()

    cursor.execute(
        '''truncate table firstapp_ssb_trans''')
    row = cursor.fetchall()

    context = {
        "row": row
    }
    return render(request, "drop_table.html", context)

def drop_ssb_balance(request):

    cursor = connection.cursor()

    cursor.execute(
        '''truncate table firstapp_ssb_balance''')
    row = cursor.fetchall()

    context = {
        "row": row
    }
    return render(request, "drop_table.html", context)






#select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_gs_tran.product_id from firstapp_tradar_tran inner join firstapp_gs_tran on firstapp_tradar_tran.cashflow = firstapp_gs_tran.netAmt where firstapp_tradar_tran.account="GS";
def test(request) :

    cursor = connection.cursor()

    cursor.execute('''select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_gs_tran.product_id, firstapp_gs_tran.brokerDesc from firstapp_tradar_tran inner join firstapp_gs_tran on firstapp_tradar_tran.cashflow = firstapp_gs_tran.netAmt where firstapp_tradar_tran.account="GS"''')
    row = cursor.fetchall()

    context = {
    "row": row
    }

    return render(request, "list.html", context)

#select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_ssb_trans.isin, firstapp_ssb_trans.sedol, firstapp_tradar_tran.description,firstapp_tradar_tran.type from firstapp_tradar_tran inner join firstapp_ssb_trans on firstapp_tradar_tran.cashflow = firstapp_ssb_trans.net_amt where firstapp_tradar_tran.account="SS";
def tradar_ss_trans_inis(request) :

    cursor = connection.cursor()
    # cursor.execute('''select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_gs_tran.product_id from firstapp_tradar_tran inner join firstapp_gs_tran on firstapp_tradar_tran.cashflow = firstapp_gs_tran.netAmt where firstapp_tradar_tran.account="GS";"''')
    # row = cursor.fetchone()
    # with connection.cursor() as cursor:
    cursor.execute('''select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_ssb_trans.isin, firstapp_ssb_trans.sedol, firstapp_tradar_tran.description,firstapp_tradar_tran.type from firstapp_tradar_tran inner join firstapp_ssb_trans on firstapp_tradar_tran.cashflow = firstapp_ssb_trans.net_amt where firstapp_tradar_tran.account="SS";''')
    row = cursor.fetchall()

    context = {
    "row": row
    }
    return render(request, "tradar_ss_isin.html", context)


#------------------
def tradar_gs_trans_ccy(request) :

    cursor = connection.cursor()

    cursor.execute('''select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_gs_tran.product_id, firstapp_gs_tran.brokerDesc,firstapp_tradar_tran.ccy,firstapp_gs_tran.currency from firstapp_tradar_tran inner join firstapp_gs_tran on firstapp_tradar_tran.cashflow = firstapp_gs_tran.netAmt and firstapp_tradar_tran.ccy="USD" and firstapp_gs_tran.currency="U S DOLLAR" where firstapp_tradar_tran.account="GS"''')
    row = cursor.fetchall()

    context = {
    "row": row
    }
    return render(request, "tradar_gs_ccy.html", context)

#-----------------------
def tradar_ss_trans_ccy(request) :

    cursor = connection.cursor()
    # cursor.execute('''select firstapp_tradar_tran.isin, firstapp_tradar_tran.cusip, firstapp_gs_tran.product_id from firstapp_tradar_tran inner join firstapp_gs_tran on firstapp_tradar_tran.cashflow = firstapp_gs_tran.netAmt where firstapp_tradar_tran.account="GS";"''')
    # row = cursor.fetchone()
    # with connection.cursor() as cursor:
    cursor.execute('''select firstapp_tradar_tran.isin, firstapp_tradar_tran.description,firstapp_tradar_tran.type,firstapp_tradar_tran.ccy,firstapp_ssb_trans.currency from firstapp_tradar_tran inner join firstapp_ssb_trans on firstapp_tradar_tran.cashflow = firstapp_ssb_trans.net_amt and firstapp_tradar_tran.ccy = firstapp_ssb_trans.currency where firstapp_tradar_tran.account="SS";''')

    row = cursor.fetchall()

    context = {
    "row": row
    }
    return render(request, "tradar_ss_ccy.html", context)

#select firstapp_ssb_balance.fund, firstapp_ssb_balance.currency, firstapp_ssb_balance.amount from firstapp_tradar_balance inner join firstapp_ssb_balance on firstapp_tradar_balance.balance = firstapp_ssb_balance.amount having firstapp_ssb_balance.amount <> 0;
def tradar_ss_bal(request) :

    cursor = connection.cursor()

    cursor.execute('''select firstapp_ssb_balance.fund, firstapp_ssb_balance.currency, firstapp_ssb_balance.amount from firstapp_tradar_balance inner join firstapp_ssb_balance on firstapp_tradar_balance.balance = firstapp_ssb_balance.amount having firstapp_ssb_balance.amount <> 0;''')
    row = cursor.fetchall()

    context = {
    "row": row
    }
    return render(request, "tradar_ss_bal.html", context)

#select firstapp_gs_balance.acc_no, firstapp_gs_balance.acc_name, firstapp_gs_balance.td_quantity, firstapp_tradar_balance.balance from firstapp_tradar_balance inner join firstapp_gs_balance on firstapp_tradar_balance.balance = firstapp_gs_balance.sd_quantity having firstapp_tradar_balance.balance <> 0;
def tradar_gs_bal(request) :

    cursor = connection.cursor()

    cursor.execute('''select firstapp_gs_balance.acc_no, firstapp_gs_balance.acc_name, firstapp_gs_balance.td_quantity, firstapp_tradar_balance.balance from firstapp_tradar_balance inner join firstapp_gs_balance on firstapp_tradar_balance.balance = firstapp_gs_balance.sd_quantity having firstapp_tradar_balance.balance <> 0;''')
    row = cursor.fetchall()

    context = {
    "row": row
    }
    return render(request, "tradar_gs_bal.html", context)