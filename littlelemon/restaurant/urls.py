
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views 

urlpatterns = [
    path('menu/',views.MenuItem.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),    
    path('api-token-auth/', obtain_auth_token)
    ]