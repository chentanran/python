from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300) # 规定了字段title的属性为CharField()类型，并且以参数max_length=300的形式说明字段的最大数量
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') # ForeignKey()就反映了这种“一对多”, on_delete是必不可少的一个参数（对于Django2.x版本），其值通常为models.CASCADE，含义是“级联删除,related_name="blog_posts"的作用是允许类User的实例（某个用户名）以“blog_posts”属性反向查询到类BlogArticles的实例
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)  # 通过ordering =("-publish", )规定了BlogArticles实例对象的显示顺序，即按照publish字段值的倒序显示。

    def __str__(self):
        return self.title
