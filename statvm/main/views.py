from django.shortcuts import render
from flask import Flask, render_template
from django.http import HttpResponse
import random
def index(request):
    a = random.randint(1,10)
    data = {"message": a}
    return render(request,'main/index.html', context=data)

def about(request):
    return render(request,'main/about.html')
