from django.conf.urls import url
from django.contrib import admin

from forms1 import views
from midd import views as v

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index, name='index'),
    url('test/', v.test1),
]
