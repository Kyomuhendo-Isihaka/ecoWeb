from django.db import models

# Create your models here.

class customer_req(models.Model):
    customer_name=models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    Location = models.CharField(max_length=100)

    class Meta:
        db_table ="customer_req"