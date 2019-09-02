from django.shortcuts import render

# Create your views here.
from django.views import View
from core.models import Photo

class IndexView(View):
    def get(self, request):
        my_photos = Photo.objects.all()
        return render(
            request, 'index.html', {'photos': my_photos})

from core.forms import PhotoForm
from django.views.generic import FormView
class AddPhotoView(FormView):
    template_name = "add_photo.html"
    success_url = '/'
    form_class = PhotoForm
    def form_valid(self, form):
        form.save()
        return super(AddPhotoView, self).form_valid(form)


