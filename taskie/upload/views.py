from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import UploadModel
import mimetypes

@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(View):
    def post(self, request, *args, **kwargs):
        upload = request.FILES.get("file")
        if not upload:
            return JsonResponse({"error": "Нет файла"}, status=400)

        obj = UploadModel.objects.create(
            name=upload.name,
            file=upload
        )

        mime, _ = mimetypes.guess_type(obj.file.url)
        if mime:
            if mime.startswith("image/"):
                file_type = "image"
            elif mime.startswith("video/"):
                file_type = "video"
            elif mime.startswith("audio/"):
                file_type = "audio"
            else:
                file_type = "document"
        else:
            file_type = "document"

        return JsonResponse({
            "file_url": obj.file.url,
            "file_name": obj.name,
            "file_type": file_type
        })
