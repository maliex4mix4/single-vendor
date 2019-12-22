from django.contrib import admin

# Register your models here.
from .models import Users, Cart

admin.site.register(Users)
admin.site.register(Cart)