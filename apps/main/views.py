from django.shortcuts import render
from django.views.decorators.cache import cache_page

from apps.main.models import Navigation, Category, Banner


# @cache_page()
# Create your views here.
def index(request):
    nav_list = Navigation.objects.all()
    cate_list = Category.objects.all()
    banner_list = Banner.objects.all()
    try:
        for cate in cate_list:
            shops = cate.shop_set.all()
            for shop in shops:
                shop.img = shop.image_set.values_list('shop_img_id', flat=True).first()
            cate.shops = shops
    except Exception as e:
        pass
    return render(request, 'index.html', locals())
