from django.shortcuts import render

# Create your views here.
from apps.main.models import Shop, Image, PropertyValue, Review


def detail(request):
    shop_id = request.GET.get('sid')
    if shop_id:
        # 返回列表套字典对象
        try:
            shops = Shop.objects.filter(shop_id=shop_id).values('shop_id',
                                                                'promote_price',
                                                                'original_price',
                                                                'stock',
                                                                'name',
                                                                'sub_title', )
            if shops.exists():
                shop = shops.first()
                imgs = Image.objects.filter(shop_id=shop.get('shop_id')).values('shop_img_id', 'type')
                shop.update(imgs=imgs)
                values = PropertyValue.objects.filter(shop_id=shop_id)
                reviews = Review.objects.filter(shop_id=shop_id)
                return render(request, "detail.html", locals())
        except Exception as e:
            print(e)
            return render(request, 'error.html')

    return render(request, 'error.html')
