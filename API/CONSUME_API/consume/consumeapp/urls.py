from django.conf.urls import url
from consumeapp import views
urlpatterns = [
    url(r'', views.users,name="users"),
]