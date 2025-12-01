from django.urls import path
from .import views
urlpatterns=[
    path('register/',views.reg,name="register/"),
    path('login/',views.login,name="login"),
    path('get/',views.get_data,name="get"),
    path('del/',views.delete_data,name="del"),
    path('put/',views.update_data,name="put"),
]