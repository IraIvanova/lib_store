from files.forms import FileForm
from files.utils import generate_unique_filename


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            file_instance = form.save(commit=False)
            file_instance.file.name = f"{generate_unique_filename(uploaded_file)}"
            file_instance.save()

            return file_instance

    return False
