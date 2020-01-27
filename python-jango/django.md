建立虚拟环境
```python
    python -m venv 11_env
```
激活虚拟环境
```python
    linux
        source 11_env/bin/activate
    window
        11_env\Scripts\activate
```
停止虚拟环境
```python
    deactivate
```
安装 Django
```
    pip install Django
    Django仅在虚拟环境处于活动状态时才可用
```
新建一个目录
```
    django-admin startproject learning_log
```
创建数据库
```
    python manage.py migrate
```
指定端口
```
    python manage.py runserver 8001
```
建立创建应用程序所需的基础设施
```
   python manage.py startapp learning_logs 
```
核实Django是否正确地创建了项目
```
    python manage.py runserver
```
创建超级用户
```
    python manage.py createsuperuser
    账号 11_admin
    密码 111111
```

django-admin
```
  它是Django的任务管理命令行工具

  startapp这个参数也是用于创建应用的
  manage.py在项目的根目录中被自动生成，它是对django-admin.py的简单封装,对于项目根目录中的manage.py文件，不要修改，也不要删除，后面我们会经常使用它
  mysite是所建项目的管理功能目录
    settings.py：这个文件中包括了项目的初始化设置，可以针对整个项目进行有关参数配置，比如配置数据库、添加应用等
    urls.py：这是一个URL配置表文件（或称为“模块”，在Python中，模块就是程序文件。此URL配置文件/模块，英文表示为URLconf，即URL configureation），主要将URL映射到应用程序上。当用户请求某个URL时，Django项目会根据这个文件中的映射关系指向某个目标对象，该对象可以是某个应用中的urls.py文件，也可以是某个具体的视图函数
    wsgi.py:WSGI是Web Server Gateway Interface的缩写。读者可能听说过CGI, CGI是Common Gateway Interface的缩写，与WSGI有所不同。WSGI是Python所选择的服务器和应用标准，Django也会使用。wsgi.py文件定义了我们所创建的项目都是WSGI应用
    __pycache__：如果创建项目后，不执行python manage.py runserver命令，不在浏览器中查看网站是否运行，那么它是不存在的。只有网站运行后，它才会出现。它其实是一个编译后的文件夹。看一下里面的文件，都是以．pyc结尾的文件
```
blog
```
     admin.py：在这个文件中，可以自定义Django管理工具，比如设置在管理界面能够管理的项目，或者通过重新自定义与系统管理有关的类对象，向管理功能增加新的内容
     apps.py：这个文件是Django 1.10之后增加的，通常包含对应用的配置，比如为管理功能提供一个合适的应用名称
    migrations：这是一个目录，用于存储应用的数据库表结构的指令，通过这些指令可以修改和创建数据库，从而在models.py模型类和数据库表之间迁移
    models.py：这是应用的数据模型，每个Django应用都应当有一个models.py文件，虽然该文件可以为空，但不宜删除   
     tests.py：在这个文件中可以编写测试文档来测试所建立的应用
    views.py：这是一个重要的文件，用于保存响应各种请求的函数或者类。如果编写的是函数，则称为基于函数的视图；如果编写的是类，则称为基于类的视图。views.py就是保存函数或者类的视图文件。当然，也可以用其他的文件名称，只不过在引入相应函数或者类时，要注意名称的正确性，views.py是我们习惯使用的文件名称
```     
/mysite/settings.py
```
   DEBUG：其值为True或者False。在开发过程中，需要设置成True，在调试（debugging，详见https://en.wikipedia.org/wiki/Debugging）时，Django能够显示详细的报错信息——这是“开发模式”。如果将项目部署到真正要对外发布的服务器上，我们称为“生产环境”，必须将其值修改为False，从而避免暴露项目的内部信息
     ALLOWED_HOSTS：在DEBUG为True时，其值可以为空。当部署到生产环境中时，要把主域名填写到这里，才能通过域名访问到本网站
    INSTALLED_APPS：这是一个非常重要的配置项，所有的应用只有写到这里才能生效。在默认情况下，已经有了一些应用，比如django.contrib.admin就是针对项目后台管理的应用。现在需要把刚刚建立的应用blog配置到这里。在下面的INSTALLED_APPS列表中，①是新增加的，就是所建立的应用名称，其他各项是Django默认具有的应用  
    DATABASES：在这里可以配置数据库。Django能够支持多种数据库，比如常见的MySQL、PostgreSQL、Oracle等。默认配置的是SQLite，因为这个数据库小巧灵活，还是Python标准库所支持的，所以，本书中就使用这个数据库，便于读者使用和迁移代码，在实际的工程项目中，在服务器上可能很少用到它。如果用到了别的数据库，读者可以到官方网站查阅相关配置方式（
    LANGUAGE_CODE：设置项目的语言，在一般情况下可以不用修改，如果非用汉语，则设置为LANGUAGE_CODE = 'zh-hans'（注意不是’zh-cn'）
    TIME_ZONE：设置时区，通常使用东八区，设置为“Asia/Shanghai”
```          
python manage.py makemigrations xxx
```         
   创建了一个能够建立数据库表的文件
```                 
python manage.py migrate
```
    创建数据库
```
sqlite3 db.sqlite3文件绝对目录
```
    进入终端, .tables显示当前数据库表名
    pragma table_info(blog_blogarticles); # 查看一个表的详细结构
    查看数据表
        .header on
        .mode column
        select * from 表名;

        CharField：用于保存字符串，在使用时一定要声明字符串的长度
        TextField：与CharField一样，区别在于保存的字符串长度是无限的（严格说应该受制于数据库程序和硬件系统），通常用于保存较大文本
        EmailField、URLField：都继承了CharField，只不过其中包含了验证它们的值是否是E-mail和URL的方法。将某个字段设置为该类型，不需要再编写对写入数据的验证方法
        FileField：表示该字段接收上传文件，同时将上传的文件保存到服务器中
        DateField、DateTimeField：用于保存时间，有一个常用参数auto_now_add，如果auto_now_add=True，那么当数据模型实例被保存时，当前时间将自动被存储，而不需要为该字段进行赋值。
```