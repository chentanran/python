from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 在数据库中建立的名为account_userprofile的数据库表
class UserProfile(models.Model):
    # 定义了名为user的字段，OneToOneField()的含义是通过user这个字段（作为纽带）声明UserProfile类与User类之间的关系是“一对一”的。
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    def __str__(self):
        return 'user {}'.format(self.user.username)
