from django.contrib import messages
from django.shortcuts import redirect

from apps.files.models import Files, FileTypes


def size_format(b):
    if b < 1000:
        return '%i' % b + ' B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b / 1000) + ' KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b / 1000000) + ' MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b / 1000000000) + ' GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b / 1000000000000) + ' TB'


def file_upload(request):
    if request.method == "POST":
        if request.FILES["file_name"]:
            file_text = str(request.FILES["file_name"])

            file_input = request.FILES["file_name"]

            file_type = file_text.split(".")
            file_type = file_type[1]
            file_type = FileTypes.objects.filter(text=file_type).last()

            blob = request.FILES['file_name'].read()
            file_size = len(blob)
            file_size_custom = size_format(file_size)

            files_create = Files.objects.create(
                text=file_text,
                file=file_input,
                type=file_type,
                size=file_size_custom,
                kb_size=file_size,
            )
            if files_create:
                messages.success(request, "Dosya Yükleme Başarılı")
            else:
                messages.warning(request, "Beklenmedik Bir Hata Oluştu Hata Kodu:1")
            return redirect('mainpage:index')
        else:
            messages.warning(request, "Beklenmedik Bir Hata Oluştu Hata Kodu:2")
            return redirect('mainpage:index')
    else:
        messages.warning(request, "Beklenmedik Bir Hata Oluştu Hata Kodu:3")
        return redirect('mainpage:index')
