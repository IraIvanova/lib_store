from django.shortcuts import render, redirect, get_object_or_404
import os
from .models import File
from .forms import FileForm
from .utils import check_is_file_editable, generate_unique_filename


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            uploaded_file = request.FILES['file']
            file_instance.file.name = generate_unique_filename(uploaded_file)
            file_instance.save()
            print(file_instance)

    return redirect('/')


def file_list(request):
    files = File.objects.all()
    form = FileForm()
    return render(request, 'files_list.html', {'files': files, 'form': form})
