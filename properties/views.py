from properties.models import Properties
from properties.serializers import PropertiesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db import connection

class PropertiesView(APIView):
    def get(self, request):
        max_price = request.query_params.get('max_price')
        min_price = request.query_params.get('min_price')
        area = request.query_params.get('area')
        no_of_rooms = request.query_params.get('no_of_rooms')
        city = request.query_params.get('city')
        params = []
        sql_query = "SELECT * FROM properties WHERE 1=1"
        if min_price:
            sql_query += f' AND CAST(price AS UNSIGNED) >= {min_price}'
        if max_price:
            sql_query += f' AND CAST(price AS UNSIGNED) <= {max_price}'
        if area:
            sql_query += f' AND CAST(area AS UNSIGNED) <= {area}'
        if no_of_rooms:
            sql_query += f' AND CAST(no_of_rooms AS UNSIGNED) = {no_of_rooms}'
        if city:
            sql_query += " AND address LIKE %s"
            params = [f'%{city}%']
        else:
            params = []

        sql_query += " order by price asc"
        print(sql_query)
        queryset = Properties.objects.raw(sql_query, params)
        paginator = PageNumberPagination()
        paginator.page_size = 20
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = PropertiesSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
