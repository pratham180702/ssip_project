from django.urls import path

from users import views
from .views import complaint_detail,ComplaintCreateView,ComplaintUpdateView,ComplaintDeleteView, status_change

urlpatterns = [
    path('register/', views.register, name='adminregister'),
]