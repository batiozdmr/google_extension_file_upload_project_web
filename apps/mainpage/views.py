from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.files.models import Files, TopFileTypes


@login_required
def index(request):
    files = Files.objects.filter(user=request.user)
    file_types = TopFileTypes.objects.filter()
    context = {
        'files': files,
        'file_types': file_types,
    }
    return render(request, "index.html", context)


def notFound(request):
    return render(request, "404.html", {})
