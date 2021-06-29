# -*- encoding: utf-8 -*-
"""
@Author: cuiyonghua
@CreateDate: 2021/6/28 上午10:19
@File: views.py.py
@Description: 
"""

import time
import random
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
with open('compute/my_file.txt', 'r', encoding='utf-8') as f:
    data_list = f.readlines()
    print(data_list[10])


def home(request):
    context = dict()
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    centence = random.choice(data_list)
    context['time_now'] = time_now
    context['centence'] = centence
    return render(request, 'index.html', context)


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