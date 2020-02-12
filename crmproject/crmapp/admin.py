from django.contrib import admin

from.models import Customers,Products,Orders
class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'created_date')

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'created_date')

class AdminOrder(admin.ModelAdmin):
    list_display = ('customer', 'product', 'status', 'created_date')

admin.site.register(Orders,AdminOrder)
admin.site.register(Customers,AdminCustomer)
admin.site.register(Products,AdminProduct)