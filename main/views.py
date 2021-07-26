from django.shortcuts import render
from django.http import HttpResponse


def some_shit(request):
    return HttpResponse("<h2>My first page</h2>")

def main(request):
    my_list = ['ti', 'pi', 'door']
    return render(request, 'main/main_page.html', {'context': my_list})
