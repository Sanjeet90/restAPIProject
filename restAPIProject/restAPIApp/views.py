from django.shortcuts import render, redirect
from rest_framework.views import APIView, Response, status
from django.contrib.auth import login
from .models import Employee
from .serializer import Employee_serializer
from .models import CustomUserCreationForm
from .models import User

# Create your views here.

class EmployeeDetail(APIView):
    serializer_class = Employee_serializer

    def post(self,request):
        data = {
            "ID" : request.data.get("ID",''),
            "Name" : request.data.get("Name",''),
            "Age" : request.data.get("Age",'')
        }
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            if serializer.validate_emp_id(validated_data['ID']):
                serializer.save()
                return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        EMP_ID = request.query_params.get("ID",'')
        if not EMP_ID:
            raise Exception("Please enter Employee Id")
        try:
            data = Employee.objects.filter(ID = EMP_ID).values()[0]
        except Exception as e:
            raise Response("Data is not availabe for employee id {}".format(EMP_ID),status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if data:
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response("Data is not availabe for employee id {}".format(EMP_ID))

    def put(self,request,ID):
        data = request.data
        try:
            employee = Employee.objects.get(ID = ID)
        except Exception as e:
            raise Response("No records found", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(employee, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
