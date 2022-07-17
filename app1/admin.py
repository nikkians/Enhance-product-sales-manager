from django.contrib import admin
from .models import Company_Details,Company_Customers,Company_Product
# Register your models here.

admin.site.register(Company_Details)
admin.site.register(Company_Customers)
admin.site.register(Company_Product)


admin.site.site_header = 'ElectroMonia'                   
admin.site.index_title = 'Features area'                 
admin.site.site_title = 'HTML title from adminsitration'