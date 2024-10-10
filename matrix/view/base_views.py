from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def index(request):
    return render(request, 'matrix/matrix_version.html')


def start_matrix(request):
    return render(request, 'matrix/start_matrix.html')


def test_flow(request):
    return render(request, 'matrix/test_flow.html')


def control_desk(request):
    return render(request, 'matrix/control_desk.html')


def instrument(request):
    return render(request, 'matrix/instrument.html')


def download_file(request, file_name):
    file_path = os.path.join(BASE_DIR / 'static/matrix/download', file_name)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)
        return response
    else:
        # 파일이 없을 경우 404 에러 반환
        return HttpResponse(status=404)
