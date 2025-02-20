from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    category_description = models.CharField(max_length=250, blank=True, null=True)
    category_type = models.CharField( max_length=10, choices=[('type1', 'Type1'), ('type2', 'Type2'),('type3', 'Type3')], default='type1')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.CharField(max_length=250, blank=True, null=True)
    product_qnty = models.IntegerField(default=0)
    product_type = models.CharField( max_length=10, choices=[('type1', 'Type1'), ('type2', 'Type2'),('type3', 'Type3')], default='type1')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
# Create your models here.

