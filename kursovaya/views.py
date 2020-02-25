import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .api import FileReader, GetMinimumMark, GetMaximumMark


def index(request):
    return render(request, 'index.html')


def get_file(request):
    context = {}
    file = request.FILES['statistic_file']
    if request.method == 'POST' and file:
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        _, file_ext = os.path.splitext(filename)
        uploaded_file = fs.path(filename)
        file_reader = FileReader()
        content = file_reader.read_file(uploaded_file, file_ext)
        if content:
            min_mark_cmd = GetMinimumMark()
            min_mark = min_mark_cmd.execute(content)
            max_mark_cmd = GetMaximumMark()
            max_mark = max_mark_cmd.execute(content)
            context.update({
                'min_mark': min_mark,
                'max_mark': max_mark,
            })
        else:
            context.update({
                'error_message':
                    'Неверный формат файла! Загрузите файл .txt или .csv',
            })
    return render(request, 'index.html', context)
