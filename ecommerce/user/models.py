from django.db import models
##from datetime import datetime

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.TextField()
    last_name = models.TextField()
    telephone = models.TextField()
    remember_token = models.CharField(max_length=100, null=True)
    acct_created = models.DateField(auto_now=True)
    last_login_date = models.DateField()

    def __str__(self):
        return "{}".format( self.id )

class Cart (models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    product_id = models.IntegerField()
    date_carted = models.DateField(auto_now=True)
    user_id = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return "{}".format( self.id )
