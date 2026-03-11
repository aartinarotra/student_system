from rest_framework.pagination import PageNumberPagination
class mypagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'  # ?size=5 se override kar sakte ho
    max_page_size = 10
    