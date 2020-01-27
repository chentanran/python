from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    # path('login/', views.user_login, name='user_login')
    # auth_views.LoginView.as_view()是新引入的模块中提供的登录方法
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_form.html', # 修改密码的页面模板
        success_url='/account/password-change-done' # 说明了如果密码修改成功，页面跳转对象
    ), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'
    ), name='password_change_done')
]