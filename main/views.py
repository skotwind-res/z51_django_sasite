from django.shortcuts import render


def about(request):
    return render(request, 'main/about.html')


def main(request):
    return render(request, 'main/main_page.html')


def contacts(request):
    return render(request, 'main/contacts.html')
