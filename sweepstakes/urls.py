from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_home, name='user_home'),
]
