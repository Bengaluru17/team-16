from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^signup/',views.user_signup,name='signup'),
    url(r'^level1/',views.level1,name='level1'),
    url(r'^logout/',views.logout_view,name='logout')
]