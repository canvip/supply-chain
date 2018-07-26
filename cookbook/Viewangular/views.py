from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class FrontendRenderView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html",{})
    def get(self, request, *args, **kwargs):
        return render(request, "index.html",{})








