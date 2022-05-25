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
    bytes_data = request.body
    stream = io.BytesIO(bytes_data)
    print(stream)
    data = JSONParser().parse(stream)
    # print(data)

    return HttpResponse("Hello")