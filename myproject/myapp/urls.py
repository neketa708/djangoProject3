from django.urls import path
from .views import index, about
from .views import year_post, MonthPost, ClientOrderItemsView

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/<int:year>/', year_post, name='year_post'),
    path('post/<int:year>/<int:month>/', MonthPost.as_view, name='mont_post'),
    path('client_order_items/', ClientOrderItemsView.as_view(), name='client_order_items'),
]