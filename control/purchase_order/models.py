from django.db import models


class Supplier(models.Model):

    supplier_name = models.CharField(null=False, blank=False, max_length=100)
    supplier_ref = models.CharField(null=True, blank=True, max_length=100)
    contact = models.CharField(null=True, blank=True, max_length=100)
    address = models.CharField(null=True, blank=True, max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    supplier_email = models.EmailField(null=True, blank=True)


class PurchaseOrder(models.Model):

    quantity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True, max_length=100)
    unit_cost = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    total = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    vat = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=20)
    comments = models.TextField(blank=True, null=True, max_length=200)
    purchase_date = models.DateField(blank=False, null=False)
    status = models.CharField(max_length=10, choices=(('created', 'Created'),
                                                      ('approved', 'Approved')))
    supplier = models.ForeignKey(Supplier)
    purchase_order_number = models.CharField(blank=False, null=False, max_length=10)
    currency = models.CharField(max_length=10, choices=(('pounds', 'Pounds'),
                                                        ('dollars', 'Dollars'),
                                                        ('euros', 'Euros')))