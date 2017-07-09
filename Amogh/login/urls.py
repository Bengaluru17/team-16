from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^signup/',views.user_signup,name='signup'),
    url(r'^level1/',views.level1,name='level1'),
    url(r'^level2/',views.level2,name='level2'),
    url(r'^level3',views.level3,name='level3'),
    url(r'^level4',views.level4,name='level4'),
    url(r'^level5',views.level5,name='level5'),
    url(r'^logout/',views.logout_view,name='logout'),
    url(r'^adminLogin/',views.admin_login,name='adminLogin'),
    url(r'^adminsignup',views.admin_signup,name='adminsignup')
]