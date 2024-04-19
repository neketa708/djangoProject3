import logging
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import render

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

class ClientOrderItemsView(TemplateView):
    template_name = 'myapp/client_order_items.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.request.user  # предполагается, что пользователь был аутентифицирован
        ordered_products = []
        orders = client.orders.filter(date__gte=timezone.now() - timezone.timedelta(days=365)).order_by('-date')

        last_7_days_items = self.get_items_in_period(orders, 7, ordered_products)
        last_30_days_items = self.get_items_in_period(orders, 30, ordered_products)
        last_365_days_items = self.get_items_in_period(orders, 365, ordered_products)

        context['last_7_days_items'] = last_7_days_items
        context['last_30_days_items'] = last_30_days_items
        context['last_365_days_items'] = last_365_days_items

        return context

    def get_items_in_period(self, orders, days, ordered_products):
        items = []
        for order in orders.filter(date__gte=timezone.now() - timezone.timedelta(days=days)):
            for product in order.products.all():
                if product not in ordered_products:
                    items.append(product)
                    ordered_products.append(product)
        return items