import logging
from django.http import  HttpResponse
from django.views.generic import TemplateView

_logger = logging.getLogger(__name__)

def maintenance(request,cheneso):
    _logger.warning(request)
    return HttpResponse(f"Tutto ok {cheneso}")

class Maintenance(TemplateView):
    template_name = 'Maintenance.html'

class NotFound(TemplateView):

    template_name = '404.html'

class Homepage(TemplateView):

    template_name = 'home.html'