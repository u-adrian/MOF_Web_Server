from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'test_ai/index.html', context)


def upload(request):
    result = {}
    if request.method == "POST":
        upload_file = request.FILES['document']
        print(upload_file.name)
        print(upload_file.size)
        file_content = upload_file.read()
        result = {'file_content': file_content}
    return render(request, 'test_ai/upload.html', result)
