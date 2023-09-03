

from django.urls import path
from . import views 

urlpatterns = [
    path('menu/',views.MenuItem.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),    
]