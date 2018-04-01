from django.shortcuts import render,HttpResponse
import time
# from django.views.decorators.cache import cache_page
#
#
# @cache_page(5)
# def index(request):
#     ctime = time.time()
#     return render(request,'index.html',{'ctime': ctime})


def index(request):
    ctime = time.time()
    return render(request,'index.html',{'ctime': ctime})


def new(request):
    ctime = time.time()
    return HttpResponse(ctime)