from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse


def index(request):
    return render(request, 'contourshow/contour_show_main.html')


