from django.db import models

class Supplier(models.Model):

    supplier_name = models.CharField(max_length=100)
    supplier_ref = models.CharField(null=True, blank=True, max_length=100)
    contact = models.CharField(null=True, blank=True, max_length=100)
    address = models.CharField(null=True, blank=True, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=15)
    fax = models.CharField(null=True, blank=True, max_length=30)
    supplier_email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.supplier_name


class Item(models.Model):

    quantity = models.IntegerField()
    description = models.TextField(max_length=100)
    unit_cost = models.DecimalField(decimal_places=2, max_digits=20)


class PurchaseOrder(models.Model):

    item = models.ForeignKey(Item)
    vat = models.DecimalField(decimal_places=2, max_digits=20, default=0.0)
    comments = models.TextField(max_length=200)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('created', 'Created'),
                                                      ('approved', 'Approved')))
    supplier = models.ForeignKey(Supplier)
    purchase_order_number = models.CharField(blank=False, null=False, max_length=10)
    currency = models.CharField(max_length=10, choices=(('pounds', 'Pounds'),
                                                        ('dollars', 'Dollars'),
                                                        ('euros', 'Euros')))

    # def vat_total(self):
    #     return self.quantity * self.unit_cost * self.vat
    #
    # def total_cost(self):
    #     return self.unit_cost * self.quantity
    #
    # def total_cost_with_vat(self):
    #     return self.vat_total() + self.total_cost()


