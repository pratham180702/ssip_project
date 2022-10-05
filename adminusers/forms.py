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
        fields = ['username','first_name','email','middle_name', 'last_name', 'username','category_select', 'address']