from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GS_Tran,Tradar_Tran,SSB_Trans,SSB_Balance,GS_Balance,Tradar_Balance

admin.site.register(GS_Tran)
admin.site.register(Tradar_Tran)
admin.site.register(SSB_Trans)
admin.site.register(SSB_Balance)
admin.site.register(GS_Balance)
admin.site.register(Tradar_Balance)
