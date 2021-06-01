from django.db import models
from django.db.models.deletion import SET_NULL
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from slugify import  slugify_unicode
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, verbose_name="أسم المستخدم", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    #device = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        if self.user:
            name = str(self.user)
        else:
            name = self.device
        return str(name)
        
def image_upload(instance, filename):
    imageName, extension = filename.split('.')
    return "products/%s/%s/%s.%s"%(instance.ProBrand,instance.ProCtegory,instance.ProName ,extension)

class Product(models.Model): # the prodact is a main class 
    ProName = models.CharField(max_length=150, unique=True, verbose_name='اسم المنتج كامل')
    ProCtegory = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, verbose_name="نوع المنتج")
    ProBrand = models.ForeignKey('brands.Brand', related_name='Brands', on_delete=models.CASCADE, blank=True, null=True, verbose_name="الماركة")
    # ProAlternatve = 
    ProDesc = RichTextField(verbose_name="تفاصيل المنتج")
    ProStock = models.BooleanField(default=True, blank=True, null=True, verbose_name="المخزون")
    ProPrice = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="سعر السوق")
    ProDiscountPrice = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="السعر بعد الخصم", default=0, blank=True, null=True)
    ProImg_1 = models.ImageField(upload_to=image_upload, blank=True, null=True, default = '../static/assets/images/no-image.jpg', max_length=250, verbose_name='الصورة الرئيسية')
    ProImg_2 = models.ImageField(upload_to=image_upload, blank=True, null=True, default = '../static/assets/images/no-image.jpg', max_length=250, verbose_name='الصورة الفرعية')
    ProCreated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(blank=True, null=True, verbose_name="URl")

    def save(self,*args, **kwargs):
        if not self.slug :
            self.slug = slugify_unicode(self.ProName, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("Product:productDetail", kwargs={"slug": self.slug})
    
    def get_add_to_cart_url(self):
        return reverse("Product:add_to_cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("Product:remove_from_cart", kwargs={"slug": self.slug})
    
    def get_category_url(self):
        return reverse("Product:products")

    def __str__(self):
        return self.ProName

        
class Category(models.Model):
    CatName = models.CharField(max_length=50, verbose_name = 'نوع المنتج')

    def __str__(self):
        return self.CatName

class OrderItem(models.Model):
    user = models.ForeignKey(User, verbose_name="أسم المستخدم", on_delete=SET_NULL, blank=True, null=True)
    item = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"

    def __str__(self):
        return f"{self.quantity} of {self.item.ProName}"

    def totle_price_discount(self):
        return self.quantity * self.item.ProDiscountPrice
    
    def totle_price(self):
        return self.item.ProPrice * self.quantity

    def totle_saving_price(self):
        return self.totle_price() - self.totle_price_discount()

    def get_finla_price(self):
        if self.item.ProDiscountPrice:
            return self.totle_price_discount()
        return self.totle_price()

    def get_finla_price_saving(self):
        if self.item.ProDiscountPrice:
            return self.totle_saving_price()
        return 0
           

class Order(models.Model):
    """Model definition for Order."""
    OrdName = models.ForeignKey(User, verbose_name="أسم المستخدم", on_delete=SET_NULL, blank=True, null=True)
    items = models.ManyToManyField(OrderItem, verbose_name="المنتجات المطلوبة")
    OrdStartDate = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ اضافة المنتج")
    OrdOrderedDate = models.DateTimeField()
    OrdOrdered = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return self.OrdName.user.username

    def get_total(self):
        total = 0
        for total_item in self.items.all():
            total += total_item.get_finla_price()
        return total

    def get_total_saving(self):
        total = 0
        for total_item in self.items.all():
            total += total_item.get_finla_price_saving()
        return total

###
##### Alternatve it may be opened in the future
###
# class ProductAlternative(models.Model):
#     PrAlName = models.ForeignKey(Product, related_name='choose_product', on_delete=models.CASCADE, verbose_name="المنتج")
#     PrAlternative = models.ManyToManyField(Product, related_name="product_with_alternative", verbose_name="بدائل المنتج")

#     class Meta:
#         verbose_name = "ProductAlternative"
#         verbose_name_plural = "ProductAlternatives"

#     def __str__(self):
#         return str(self.PrAlName)
