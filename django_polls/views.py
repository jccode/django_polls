from django.shortcuts import render_to_response
from django.views.generic import TemplateView


def index(request):
    """
    """
    # return TemplateView.as_view(template_name="index.html")
    return render_to_response("index.html")
    

