from django.urls import path
from .views import index,paras,greet

urlpatterns = [
    path("", index, name="index"),
    path("paras",paras,name="paras"),
    path("<str:name>",greet,name="greet")
]
