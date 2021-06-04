# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProductSku(models.Model):
    sku_id = models.UUIDField(primary_key=True)
    owner_id = models.UUIDField()
    sku = models.TextField()
    status = models.IntegerField()
    prod_id = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'product_sku'


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    origname = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    uid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'products'


class Properties(models.Model):
    prop_id = models.UUIDField()
    origname = models.TextField(blank=True, null=True)
    prop_type = models.IntegerField(blank=True, null=True)
    prop_group_id = models.UUIDField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'properties'
