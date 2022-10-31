from django.http import HttpResponse
from django.views.generic import ListView

from .models import Employee


class EmployeeView(ListView):

    model = Employee
    context_object_name = 'employees'
    template_name = 'employees-list.html'

    def get_queryset(self):
        return Employee.objects.all()
