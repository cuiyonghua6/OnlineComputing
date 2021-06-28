# -*- encoding: utf-8 -*-
"""
@Author: cuiyonghua
@CreateDate: 2021/6/28 上午10:19
@File: views.py.py
@Description: 
"""
import datetime
from django.http import HttpResponse
from django.shortcuts import render


def app_normal(request):
    return HttpResponse("app normal--- ")


from django.shortcuts import render
import subprocess
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    return render(request, 'index.html')


def run_code(code):
    try:
        code = 'print(' + code + ')'
        output = subprocess.check_output(['python', '-c', code],
                                         universal_newlines=True,
                                         stderr=subprocess.STDOUT,
                                         timeout=30)
    except subprocess.CalledProcessError as e:
        output = '公式输入有误'
    return output


@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result': result})