import xadmin
from xadmin import views
from xadmin.plugins import auth

from apps.main.models import *


class BaseStyleSetting:
    # 开启主题修改
    enable_themes = True
    # 可以使用bootstrap的主题
    use_bootswatch = True


# 注册自定义全局配置
xadmin.site.register(views.BaseAdminView, BaseStyleSetting)


class GlobalSettings:
    # 修改标题
    site_title = '91商城后台管理'
    # 修改底部显示
    site_footer = '91集团'


xadmin.site.register(views.CommAdminView, GlobalSettings)


# 用户管理
class UserAdmin(auth.UserAdmin):
    list_display = ['id', 'username', 'email', 'img_show']


# 先注销
xadmin.site.unregister(User)
# 再注册
xadmin.site.register(User, UserAdmin)


# 导航
class NavigationAdmin:
    # 设置后台默认情况下显示objaect对象
    list_display = ['nav_id', 'nav_name']


xadmin.site.register(Navigation, NavigationAdmin)


# 商品管理
class ShopAdmin:
    list_display = ['shop_id', 'name', 'create_date']
    # 修改分页
    list_per_page = 10
    # 搜索字段
    search_fields = ['name', 'sub_title']
    list_editor = []


xadmin.site.register(Shop, ShopAdmin)


# 用户评论
class ReviewAdmin:
    list_dispaly = ['review_id', 'content', 'create_date', 'shop']


xadmin.site.register(Review, ReviewAdmin)


# 轮播图
class BannerAdmin:
    list_display = ['banner_id', 'title', 'image', 'create_time']


xadmin.site.register(Banner, BannerAdmin)


# 分类
class CategoryAdmin:
    list_display = ['cate_id', 'name']


xadmin.site.register(Category, CategoryAdmin)


# 订单管理
class OrderAdmin:
    list_display = ['oid', 'order_code', 'address',
                    'post', 'receiver ', 'mobile', 'user_message', 'create_date', 'pay_date status']


xadmin.site.register(Order, OrderAdmin)


# 商品属性
class PropertyAdmin:
    list_display = ['property_id', 'name', ]


xadmin.site.register(Property, PropertyAdmin)


# 商品属性值
class PropertyValueAdmin:
    list_display = ['shop', 'property', 'value', ]


xadmin.site.register(PropertyValue, PropertyValueAdmin)


# 购物车
class ShopCarAdmin:
    list_display = ['car_id', 'number', 'shop', 'user', 'order']


xadmin.site.register(ShopCar, ShopCarAdmin)


# 图片管理
class ImageAdmin:
    list_display = ['shop', 'type']
    search_fields = ['name', 'sub_title']
    list_editor = []


xadmin.site.register(Image, ImageAdmin)


# 一级菜单管理
class SubMenuAdmin:
    list_display = ['sub_menu_id', 'name', 'cate']


xadmin.site.register(SubMenu, SubMenuAdmin)


# 二级菜单管理
class SubMenu2Admin:
    list_display = ['sub_menu2_id', 'name']


xadmin.site.register(SubMenu2, SubMenu2Admin)
