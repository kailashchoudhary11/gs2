from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 

import json
import io
# Create your views here.

def student_details(request, id):
    student = Student.objects.get(id = id)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type= "application/json")

@csrf_exempt
def create_student(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        # print(stream.getvalue())
        pythondata = JSONParser().parse(stream)
        print(type(pythondata))
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            print("helk")
            serializer.save()
            res = {"msg": "Data Created"}
            return JsonResponse(res)
        print("Hok")
        return JsonResponse(serializer.errors)