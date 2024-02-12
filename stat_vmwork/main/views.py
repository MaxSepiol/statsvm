from django.shortcuts import render
from flask import Flask, render_template
from django.http import HttpResponse
import random
import time
from django.http import HttpResponse, HttpResponseRedirect
import chartkick.django


def index(request):
    return render(request,'main/index.html')

def timefun(request):
    if request.method == "POST":
        time.sleep(1)
        with open("1.txt","w") as f:
            f.write("4456")
        a = time.time()
        print(a)
        next = request.POST.get('next', '/stat')
        return HttpResponseRedirect(next)
    #return render(request,'main/index.html')


def stat(request):
    chart = chartkick.django.PieChart({'gow': 1, 'gow2': 1, 'gow3': 6, 'gow4': 9},width=300,height=300,
                                      colors=['#48cae4', '#0077b6', '#023e8a'], pieSliceText='Value', dataset={'borderWidth': 5}, legend='right', min=0, max=10)
    return render(request, 'main/stat.html', {'chart': chart})
def about(request):
    return render(request,'main/about.html')
