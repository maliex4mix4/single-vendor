from django.urls import path
from .views import loginDisp, registerDisp

urlpatterns = [
    path('login/', loginDisp)
]
