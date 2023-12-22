from django.urls import path

from . import views


urlpatterns = [
    path('buy/<int:item_id>', views.buy, name='buy'),
    path('item/<int:item_id>', views.item, name='item'),
]
