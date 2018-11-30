from django.contrib import admin

from control.purchase_order.models import Supplier, PurchaseOrder


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ['id', 'supplier_name']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'purchase_order_number']