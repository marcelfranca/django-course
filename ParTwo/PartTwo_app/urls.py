from django.urls import re_path
from PartTwo_app import views

urlpatterns = [
    re_path(r'^$',views.help,name='help'),
]
