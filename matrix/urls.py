from django.urls import path
from .view.base_views import *

app_name = 'matrix'

urlpatterns = [
    path('', index, name='index'),
    path('program_guide/<str:name>/', program_guide, name='program_guide'),
    path('tuner_management/<str:name>/', tuner_management, name='tuner_management'),
    path('register/<str:name>/', register, name='register'),
    path('calibration/<str:name>/', calibration, name='calibration'),
    path('csv_harmonic/<str:name>/', csv_harmonic, name='csv_harmonic'),
    path('gain_sweep/<str:name>/', gain_sweep, name='gain_sweep'),
    path('pa_ruggedness/<str:name>/', pa_ruggedness, name='pa_ruggedness'),
    path('common_trx_plan/<str:name>/', common_trx_plan, name='common_trx_plan'),
    path('data_analysis/<str:name>/', data_analysis, name='data_analysis'),
    path('simple_function/<str:name>/', simple_function, name='simple_function'),
    path('general_measurements/<str:name>/', general_measurements, name='general_measurements'),
    path('traditional_csv/<str:name>/', traditional_csv, name='traditional_csv'),
    path('special_test/<str:name>/', special_test, name='special_test'),
    path('download/<str:file_name>/', download_file, name='download_file'),
]
