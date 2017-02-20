from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Harris!! A view!")

def farewell(request):
    return HttpResponse("A dieu World!")

def table(request):
    df = pd.DataFrame(np.random.randn(10, 5),
    columns = list("abcde"))
    table = df.to_html()
    return HttpResponse(table)

from os.path import join
from django.conf import settings
import pandas as pd

def csv(request):
    baby = join(settings.STATIC_ROOT , ' myapp/baby.csv ' )
    df = pd.read_csv(baby)
    return HttpResponse(df.to_html())

def greet(request, who):
    return HttpResponse("Hello" + who)

def add(request, n1, n2):

    n1, n2 = int(n1), int(n2)
    return HttpResponse(str(n1 + n2))
# http does not take integers, thus you need to string your integers.
