from .serializers import EmployeeSerializer
from .models import Employee
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Get request for getting polls of all employees
# Post request for adding new employee
@csrf_exempt
@api_view(['GET', 'POST'])
def polls(request):
    if request.method == "GET":
        all_employees_data = Employee.objects.all()
        serializer = EmployeeSerializer(all_employees_data, many=True)
        return Response(serializer.data, status=200)
    elif request.method == "POST":
        deserializer = EmployeeSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.validated_data, status=201)
        return Response(deserializer.errors, status=400)


# Get request for getting polls of Specific Employee
# Put request for updating data of existing Employee
# Delete Request for deleting data of an existing employee
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def poll_details(request, id):
    try:
        employee_obj = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = EmployeeSerializer(employee_obj)
        return Response(serializer.data, status=200)
    elif request.method == "PUT":
        deserializer = EmployeeSerializer(employee_obj, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.validated_data, status=200)
        return Response(deserializer.errors, status=400)
    elif request.method == "DELETE":
        employee_obj.delete()
        return Response(status=204)

