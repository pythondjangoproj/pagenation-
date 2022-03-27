from rest_framework.pagination import PageNumberPagination,CursorPagination
class MyPagination(PageNumberPagination):
    page_size=5

class MyPagination1(CursorPagination):
    ordering='esal'
