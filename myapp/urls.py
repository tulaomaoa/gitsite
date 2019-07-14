from . import views
from django.urls import path
app_name='myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('fruit/',views.fruit, name='fruit'),
    path('add/',views.add, name='add')

]