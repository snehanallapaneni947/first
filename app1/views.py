from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sneha(request):
    return HttpResponse('sneha is good')
def anitha(request):
    return HttpResponse('<h1>i am anitha</h1>')
def lokesh(request):
    return HttpResponse('<i>roll number 451</i>')
def apinapi(request):
    return HttpResponse('<b><i>village</i></b>')
def college(request):
    return HttpResponse('<h1>visvodaya</h1><b>kavali</b><marquee>udayagiri road</marquee>')