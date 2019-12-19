from django import forms

from .models import Users, Cart

class LoginForm(forms.Form):
    class Meta:
        model = Users
        fields = [
            'email',
            'telephone',
            'password'
        ]

class RegisterForm(forms.Form):
    class Meta:
        model = Users
        fields = [
            'email',
            'password',
            'last_name',
            'first_name',
            'acct_created',
            'telephone',
            'last_login_date'
        ]

class CartForm(forms.Form):
    class Meta:
        model = Cart
        fields = [
            'product_id',
            'date_carted',
            'user_id'
        ]
