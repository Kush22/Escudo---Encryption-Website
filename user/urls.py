from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
	#user/
	url(r'^$', views.index, name='index'),
	#user/register/
	url(r'^register/$', views.register, name='register'),
	#user/login_user/
	url(r'^login_user/$', views.login_user, name='login_user'),
	#user/logout_user
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
]