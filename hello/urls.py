from django.urls import path

from hello import views

urlpatterns=[
    path("",views.index,name="index"),
    path("index/",views.IndexView.as_view(),name="index2"),
]