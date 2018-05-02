# Django学习

## 安装、创建并启动项目

- 安装（此处使用pip安装）：`pip install Django==版本号`

- 创建项目：`django-admin startproject 项目名`

- 启动项目：`python manage.py runserver [端口号]`,若不指定端口号，则使用默认端口`8000`

## 项目结构

- `manage.py`: 项目管理器，与项目进行交互的命令行工具集的入口，执行`python manage.py`可查看所有命令

- `wsgi.py`: Python服务器网关接口

- `urls.py`: url配置文件

- `settings.py`: 项目主要配置文件, 具体看[这里](./DjangoStudy/settings.py)

## 创建应用

- 进入`manage.py`文件的目录

- 输入命令： `python manage.py startapp [项目名]`

- 将创建的应用加入`settings.py`文件内的`INSTALLED_APPS`

## 应用目录结构

- `admin.py`: 应用的后台管理系统配置

- `apps.py`: 应用的一些配置

- `models.py`: 数据模块，使用ORM框架

- `tests.py`: 自动化测试模块

- `views.py`: 执行相应代码所在的模块, 逻辑处理的主要地点

## 如何编写应用

- 在`views.py`中编写相应函数(函数必须存在一个参数，一般使用request)

```python
def index(request):
  return HttpResponse('Hello World')
```

- 在`urls.py`中配置url（建议使用include方式，该处未使用，但代码中已使用）

```python
# 引入应用的views.py
import demo.views as dv

# 配置相应函数的url
urlpatterns = [
    path('index/', dv.index),
]
```

## 创建Template

- 在应用下创建文件夹`templates`

- 在`templates`下创建HTML文件(建议在templates下再建个与应用名相同的目录)

- 在`views.py`中返回`render(request, 页面， [传递给页面的参数(字典类型)])`

如：

  - views.py

  ```python
  def index(request):
    return render(request, 'index.html', {'text': '首页'})
  ```

  - html

  ```html
   <h1>{{ text }}</h1>
  ```

## 创建Models

- 创建类，该类继承`models.Model`，该类即使一张数据表

- 在类中创建字段

## 生成数据表

- 进入`manage.py`的同级目录

- 执行`python manage.py makemigrations [应用名]`,不指明应用名，则为该项目下的所有应用

- 执行`python manage.py migrate`

## 在views中获取models的数据


