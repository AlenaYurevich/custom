from django.shortcuts import render
from .forms import CustomForm


def index(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            group = int(request.POST.get('group'))
    return render(request, 'index.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
