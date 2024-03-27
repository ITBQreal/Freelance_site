from django.urls import path
from .views import index,bots, binds

urlpatterns = [
    path('', index, name='homepage'),
    path('bots', bots, name='bots_page'),
    path('binds', binds, name='binds_page')
]