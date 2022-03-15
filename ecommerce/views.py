import logging

from django.http import  HttpResponse

_logger = logging.getLogger(__name__)

def home (request):
    _logger.warning(request)
    return HttpResponse("T")