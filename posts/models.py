import uuid
from django.db import models


class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    print(post_id)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Author', blank=True, default='')
    title = models.CharField(max_length=120, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    is_public = models.BooleanField(default=False, verbose_name='Is public')

    create_date = models.DateField(auto_now=True)
    birth_date = models.DateField(verbose_name='Date of Birth')
    death_date = models.DateField(verbose_name='Date of Death')

    objects = models

    def __str__(self):
        return self.title
