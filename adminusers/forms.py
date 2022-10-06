from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from .models import AdminUsers
from complaints.models import Category


class AdminRegister(forms.ModelForm):
    class Meta:
        model = AdminUsers
        # id = models.AutoField(primary_key=True)
        first_name = forms.CharField(max_length=100)
        email = forms.EmailField(max_length=254)
        middle_name = forms.CharField(max_length=100)
        last_name = forms.CharField(max_length=100)
        # phone_no = models.IntegerField()
        username =forms.CharField(max_length=50)
        category_select = forms.ChoiceField()
        address = forms.CharField(max_length=200)
        password=forms.CharField(widget=forms.PasswordInput())
        confirm_password=forms.CharField(widget=forms.PasswordInput())
        fields = ['username','first_name','middle_name', 'last_name', 'email','category_select', 'address','password',]
        def clean(self):
            cleaned_data = super(AdminRegister, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                    "password and confirm_password does not match"
                )

class AdminLogin(forms.ModelForm):
    # email = forms.EmailField()
    username =forms.CharField(max_length=50)
    password = forms.PasswordInput()
    # email = forms.EmailField(max_length=254)

    class Meta:
        model = AdminUsers
        fields = ['username', 'password']
