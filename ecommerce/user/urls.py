from django.urls import path
from .views import loginDisp, registerDisp
from .views import index

urlpatterns = [
    path('', index),
    path('login/', loginDisp)
]
