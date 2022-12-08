from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name='home'),
	path("add/", views.add, name='add'),
	path("sub1/", views.sub1, name='sub1'),
	path("sub2/", views.sub2, name='sub2'),
	path("sub3/", views.sub3, name='sub3'),
	path("sub4/", views.sub4, name='sub4'),
	path("sub5/", views.sub5, name='sub5'),
	path("sub6/", views.sub6, name='sub6'),
	path("sub7/", views.sub7, name='sub7'),
]

