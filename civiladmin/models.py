from django.db import models
from complaints.models import Category
# Create your models here.

class CivilAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    # email = models.EmailField()
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # phone_no = models.IntegerField()
    username = models.CharField(max_length=50)
    category_select = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name