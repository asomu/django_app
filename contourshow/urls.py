from django.urls import path
from .views import index

app_name = 'contourshow'

urlpatterns = [
    path('', index, name='index'),
]
