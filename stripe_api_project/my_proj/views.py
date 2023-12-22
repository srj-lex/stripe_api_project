from os import getenv

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
import stripe

from .models import Item


stripe.api_key = getenv("STRIPE_SECRET_KEY", "1234")
domain = getenv("DOMAIN", "http://127.0.0.1:8000")


def buy(request, item_id):
    """
    Получает Stripe Session Id для оплаты выбранного Item
    и редиректит на форму оплаты.
    """
    if request.method == "GET":
        obj = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                    "price_data": {
                        "currency": obj.currency,
                        "product_data": {
                            "name": obj.name
                        },
                        "unit_amount": obj.price * 100
                    },
                    "quantity": 1,
            }],
            mode="payment",
            success_url=domain + "/my_proj/success"
        )
        return HttpResponseRedirect(redirect_to=session.url,)
    return HttpResponseNotAllowed


def item(request, item_id):
    """
    Возвращает HTML страницу, на которой будет
    информация о выбранном Item и кнопка Buy.
    """
    if request.method == "GET":
        data = get_object_or_404(Item, id=item_id)
        template = "my_proj/item.html"
        context = {
            "item": data,
            "item_id": item_id
        }
        return render(request, template, context)
    return HttpResponseNotAllowed
