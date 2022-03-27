from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializers
from rest_framework.generics import ListAPIView
# from testapp.pagination import MyPagination1


# Create your views here.

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    # pagination_class = MyPagination1
    search_fields = ('ename',)
    ordering_fields = ('eno', 'esal',)



# Both pagenation and ordering filter can't be used at the same moment