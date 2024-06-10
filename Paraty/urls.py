from django.urls import path
from django.contrib import admin
from .views import index, add_user, add_connection, connected_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('add_user/', add_user, name='add_user'),
    path('add_connection/<int:user_id>/', add_connection, name='add_connection'),  
    path('connected_users/', connected_users, name='connected_users'),
]
