

from django.urls import path
from . import views
from jobs.views import app

urlpatterns = [
    path('',views.myblog,name='myblog'),
    path('app/',app,name='app'),
    path('<int:blog_id>/',views.detail,name='detail')
] 
