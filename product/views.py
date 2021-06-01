from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, CreateView
from . models import *
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . filters import ProductFilter
# from . forms import ProductForm

class ProductListView(ListView):
    model = Product
    paginate_by = 3
    template_name = "Product\product_list.html"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "Product\product_detail.html"

# class ProductCreateView(CreateView):
#     model = Product
#     template_name = "Product\product_list.html"



# class HomeListView(ListView):
#     queryset = Product.objects.filter(ProCtegory__icontains='screen')
#     template_name = "home.html"
def home(request):
    led = Product.objects.filter(ProCtegory__CatName='تليفزيونات LED')
    degetal = Product.objects.filter(ProCtegory__CatName='تليفزيونات ديچيتال')
    android = Product.objects.filter(ProCtegory__CatName='تليفزيونات اندرويد')
    smart = Product.objects.filter(ProCtegory__CatName='التليفزيونات الذكية')
    context = {'home':led, 'degetal':degetal, 'android':android, 'smart':smart}
    return render(request, 'Product/home.html', context)
    

class OrderSummryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(OrdName=self.request.user, OrdOrdered=False)
            context = {'object': order}
            return render(self.request, "Product\cart.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request,'انت ليس لديك منتجات مختارة')
            return redirect('/')

def cart(request):
    order = Order.objects.get(OrdName=request.user, OrdOrdered=False)
    context = {'object': order}
    return render(request, "templates/base.html", context)
    
@login_required
def add_to_cart(request, slug):
    itemed = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=itemed,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(
        OrdName=request.user,
         OrdOrdered=False
         )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=itemed.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.success(request, f"تم تحديث كمية")
            return redirect ("Product:Order_Summry_View")
        else:
            order.items.add(order_item)
            order.save()
            messages.success(request, f" تم اضافة المنتج الي العربة")
            return redirect ("Product:Order_Summry_View")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(OrdName=request.user, OrdOrderedDate=ordered_date)
        order.items.add(order_item)
        order.save()
        messages.success(request, f" تم اضافة المنتج الي العربة")
        return redirect ("Product:Order_Summry_View")

@login_required
def remove_from_cart(request, slug):
    itemed = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=itemed,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(
        OrdName=request.user,
         OrdOrdered=False
         )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=itemed.slug).exists():
            order.items.remove(order_item)
            order_item.quantity = 1
            order_item.save()
            order.save()
            messages.success(request, f"اتمسحت من العربة التسوق")
            return redirect ("Product:Order_Summry_View")
        else:
            messages.info(request, f" غير موجود في العربة")
            return redirect ("Product:productDetail", slug=slug)
    else:
        messages.info(request, f" ليس لديك منتجات في العربة")
        return redirect ("Product:productDetail", slug=slug)


@login_required
def remove_signal_item_from_cart(request, slug):
    itemed = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=itemed,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(
        OrdName=request.user,
         OrdOrdered=False
         )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=itemed.slug).exists():
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.success(request, f"اتمسحت من العربة التسوق")
            return redirect ("Product:Order_Summry_View")
        else:
            messages.info(request, f" غير موجود في العربة")
            return redirect ("Product:Order_Summry_View", slug=slug)
    else:
        messages.info(request, f" ليس لديك منتجات في العربة")
        return redirect ("Product:Order_Summry_View", slug=slug)