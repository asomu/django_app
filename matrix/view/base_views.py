from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def index(request):
    return render(request, 'matrix/matrix_version.html')


def program_guide(request, name):
    return render(request, f'matrix/1_program_guide/{name}.html')


def tuner_management(request, name):
    return render(request, f'matrix/2_tuner_management/{name}.html')


def register(request, name):
    return render(request, f'matrix/3_register/{name}.html')


def calibration(request, name):
    return render(request, f'matrix/4_calibration/{name}.html')


def csv_harmonic(request, name):
    return render(request, f'matrix/5_csv_harmonic/{name}.html')


def gain_sweep(request, name):
    return render(request, f'matrix/6_gain_sweep/{name}.html')


def pa_ruggedness(request, name):
    return render(request, f'matrix/7_pa_ruggedeness/{name}.html')


def common_trx_plan(request, name):
    return render(request, f'matrix/8_common_trx_plan/{name}.html')


def data_analysis(request, name):
    return render(request, f'matrix/9_data_analysis/{name}.html')


def simple_function(request, name):
    return render(request, f'matrix/10_simple_function/{name}.html')


def general_measurements(request, name):
    return render(request, f'matrix/11_general_measurements/{name}.html')


def traditional_csv(request, name):
    return render(request, f'matrix/12_traditional_csv/{name}.html')


def special_test(request, name):
    return render(request, f'matrix/13_special_test/{name}.html')


def download_file(request, file_name):
    file_path = os.path.join(BASE_DIR / 'static/matrix/download', file_name)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        # 파일이 없을 경우 404 에러 반환
        return HttpResponse(status=404)
