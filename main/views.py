from django.shortcuts import render
from django.http import JsonResponse
from .serializers import CommentSerializer

from .models import CommonInfo, Rubric
from .forms import NameForm

def my_apipi(request):
    if request.method == "GET":
        comments = CommonInfo.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)


def about(request):
    return render(request, 'main/about.html')


def main(request):
    data = CommonInfo.objects.order_by('-published')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            new_rubric = Rubric(name=form.cleaned_data['your_name'])
            new_rubric.save()
            return render(request, 'main/main_page.html', {'data': data, 'form': form, 'name': form.cleaned_data['your_name']})

    form = NameForm()
    return render(request, 'main/main_page.html', {'data': data, 'form': form,'name':''})


def contacts(request):
    return render(request, 'main/contacts.html')

def by_rubric(request, rubric_id):
    all_rec = CommonInfo.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    return render(request, 'main/main_page.html', {'data': all_rec, 'rub': rubrics})

