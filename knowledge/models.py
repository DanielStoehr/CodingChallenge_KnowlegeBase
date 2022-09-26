from django.db import models

# Create your models here.


class KnowlegeBase(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
