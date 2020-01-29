from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ArticleColumn(models.Model):
    # 在Django中，模型对象之间的关系可以概括为“一对一”、“一对多”和“多对多”三种关系，分别对应OneToOneField、ForeignKey、ManyToManyField
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.column
