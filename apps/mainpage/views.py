from django.shortcuts import render

from apps.files.models import Files, TopFileTypes


def index(request):
    files = Files.objects.filter()
    file_types = TopFileTypes.objects.filter()
    context = {
        'files': files,
        'file_types': file_types,
    }
    return render(request, "index.html", context)


def notFound(request):
    return render(request, "404.html", {})
