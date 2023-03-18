from collections import OrderedDict
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from users.models import User
import pandas
import datetime
import json


# Create your views here.
class PostPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'page'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('items_total', self.page.paginator.count),
            ('items_in_page', self.page_size),
            ('current_page', self.page.number),
            ('total_pages', self.page.paginator.num_pages),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PostPagination

    # file_path = "D:\MEDIA\DOCUMENTOS\ThatExcelGuy\TEG WebDev\silent-memorial\sample_data.json"
    # user_id = "1ddc7aca-838d-48bb-b963-6143f62341bc"
    # author = User.objects.get(user_id=user_id)
    # is_public = True
    #
    # with open(file_path, "r") as f:
    #     content = f.read()
    #     data = json.loads(content)
    #
    #     for row in data:
    #         print(row)
    #         title = row["title"]
    #         content = row["content"]
    #         birth_date = datetime.datetime.strptime(row["birth_date"], "%Y-%m-%d")
    #         death_date = datetime.datetime.strptime(row["death_date"], "%Y-%m-%d")
    #
    #         Post(
    #             author=author,
    #             title=title,
    #             content=content,
    #             birth_date=birth_date,
    #             death_date=death_date,
    #         )

