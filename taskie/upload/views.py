from django.shortcuts import render
from .forms import DocumentForm

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save()
            return render(request,
                        'upload/upload_success.html',
                        {'document': document}
                    )
              			
    else:
        form = DocumentForm()
    return render(request, 'upload/upload.html', {'form': form})