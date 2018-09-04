from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    #url(r'^$', views.upload_csv, name='upload_csv'),
   # url(r'^$', views.import_sheet, name="update_details"),
    url(r'^$', views.import_sheet, name="import_sheet"),
    url(r'^upload_ssb_balance', views.ssb_balance, name="upload_ssb_balance"),
    url(r'^upload_tradar_balance', views.tradar_balance, name="upload_tradar_balance"),
    url(r'^upload_gs_balance', views.gs_balance, name="upload_gs_balance"),
    url(r'^upload_tradar/', views.tradar, name="tradar"),
    url(r'^upload_ssb', views.ssb_transaction, name="ssb_transaction"),
   # url(r'^drop_table/', views.drop_table, name="drop_table"),
    url(r'^list/', views.test, name="test"),
    url(r'^tradar_ss_isin/', views.tradar_ss_trans_inis),

    url(r'^tradar_ss_ccy/', views.tradar_gs_trans_ccy),
    url(r'^tradar_ss_ccy/', views.tradar_ss_trans_ccy),

    url(r'^tradar_ss_bal/', views.tradar_ss_bal),
    url(r'^tradar_gs_bal/', views.tradar_gs_bal),

    url(r'^drop_tradar_tran/', views.drop_tradar_tran, name="drop_tradar_tran"),
    url(r'^drop_gs_balance/', views.drop_gs_balance, name="drop_gs_balance"),
    url(r'^drop_gs_tran/', views.drop_gs_tran, name="drop_gs_tran"),
    url(r'^drop_ssb_trans/', views.drop_ssb_trans, name="drop_ssb_trans"),
    url(r'^drop_ssb_balance/', views.drop_ssb_balance, name="drop_ssb_balance"),
    url(r'^drop_tradar_balance/', views.drop_tradar_balance, name="drop_tradar_balance"),


]
