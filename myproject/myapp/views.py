import logging
from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
    logger.info('index')
    return HttpResponse("Sait")

def about(View):
    def get(self, request):
        return HttpResponse("about for me")

def year_post(request, year):
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month} / {year} < br > {text}")
