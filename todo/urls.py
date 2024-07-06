

from django.urls import path
from todo import views


urlpatterns = [
    path('addtask', views.addtask, name = 'addtask'),

]
