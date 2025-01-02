from django.urls import path
from .views import EmployeeDetail

urlpatterns = [
    path('employeeDetails/',EmployeeDetail.as_view(), name= "Employee_Detail")
]
