from rest_framework import pagination

class Custompagination(pagination.PageNumberPagination):

    page_size = 2