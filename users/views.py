from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer
from .models import User


# Create your views here.
class UserPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    max_page_size = 100


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = UserPagination
