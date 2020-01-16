from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path()第一个参数为空，表示访问根，又因为在blog应用中，所以访问blog应用的根，即http://127.0.0.1:8000/blog/
    # views.blog_title声明了响应这个请求的函数
    path('', views.blog_title, name='blog_title'),
    path('<int:article_id>/', views.blog_article, name='blog_article')
]