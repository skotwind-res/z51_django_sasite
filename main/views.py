from django.shortcuts import render

from .models import CommonInfo


def about(request):
    return render(request, 'main/about.html')


def main(request):
    data = CommonInfo.objects.order_by('-published')
    return render(request, 'main/main_page.html', {'data': data})


def contacts(request):
    return render(request, 'main/contacts.html')
