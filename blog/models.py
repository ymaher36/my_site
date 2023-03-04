from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(25)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title + ' - ' + self.author.__str__()
