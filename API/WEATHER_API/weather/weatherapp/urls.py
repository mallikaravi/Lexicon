# from django.conf.urls import url
# from . import views

# urlpatterns = [
#     url(r'',views.home,name="home")
# ]



from django.conf.urls import url
from weatherapp import views
urlpatterns = [
    url(r'', views.home,name="home"),
]