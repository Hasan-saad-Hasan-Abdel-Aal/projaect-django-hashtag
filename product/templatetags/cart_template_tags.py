from django import template
from product.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
        qs = Order.objects.filter(OrdName=user, OrdOrdered=False)
        if qs.exists():
            return qs[0].items.count()
        else:
            return 0


@register.filter
def cart_item(user):
    order = Order.objects.filter(OrdName=user, OrdOrdered=False)
    if order.exists():
        return order[0].items.all()
    


