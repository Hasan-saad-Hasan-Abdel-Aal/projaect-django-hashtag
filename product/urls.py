from django.urls import path, re_path
from .views import  *

app_name = 'product'

urlpatterns = [
    # path("", HomeListView.as_view(), name="home"),
    path("", home, name="home"),
    path("products/", ProductListView.as_view(), name="products"),
    re_path(r"^product/(?P<slug>.*)/$", ProductDetailView.as_view(), name="productDetail"),
    path("Order-Summry/", OrderSummryView.as_view(), name="Order_Summry_View"),
    re_path(r"^add_to_cart/(?P<slug>.*)/$", add_to_cart, name="add_to_cart"),
    re_path(r"^remove-from-cart/(?P<slug>.*)/$", remove_from_cart, name="remove_from_cart"),
    re_path(r"^remove-signal-item-from-cart/(?P<slug>.*)/$", remove_signal_item_from_cart, name="remove_signal_item_from_cart"),
]