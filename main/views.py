from django.shortcuts import render
from django.http import HttpResponse


def some_shit(request):
    return HttpResponse("<h2>My first page</h2>")

def main(request):
    return HttpResponse("<h2>Main page</h2>")
