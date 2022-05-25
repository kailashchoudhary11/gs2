from django.contrib import admin
from api.models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ["id", "prn", "name", "city"]
    