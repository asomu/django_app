from django.urls import path
from .view.base_views import *

app_name = 'matrix'

urlpatterns = [
    path('', index, name='index'),
    path('start', start_matrix, name='start_matrix'),
    path('flow', test_flow, name='test_flow'),
    path('control', control_desk, name='control_desk'),
    path('instrument', instrument, name='instrument'),
    path('download/<str:file_name>/', download_file, name='download_file'),
]
