from django.contrib import admin
from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods,User,Cart,Order

class WheelAdmin(admin.ModelAdmin):
    list_display = ['img','name','trackid']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('trackid', 'name')


class NavAdmin(admin.ModelAdmin):
    list_display = ['img', 'name', 'trackid']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('trackid', 'name')



class MustbuyAdmin(admin.ModelAdmin):
    list_display = ['img', 'name', 'trackid']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('trackid', 'name')

class ShopAdmin(admin.ModelAdmin):
    list_display = ['img', 'name', 'trackid']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('trackid', 'name')

class MainShowAdmin(admin.ModelAdmin):
    list_display = ['trackid','name','img','categoryid','brandname','img1','childcid1','productid1','longname1','price1','marketprice1','img2','childcid2','productid2','longname2','price2','marketprice2','img3','childcid3','productid3','longname3','price3','marketprice3',]

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('trackid',)

class FoodTypesAdmin(admin.ModelAdmin):
    list_display = ['typeid','typename','typesort','childtypenames']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('typeid',)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['productid','productimg','productname','productlongname','isxf','pmdesc','specifics','price','marketprice','categoryid','childcid','childcidname','dealerid','storenums','productnum']

    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('productid', 'productname')


class UserAdmin(admin.ModelAdmin):
    list_display = ['userAccount','userPasswd','userName','userPhone','userAdderss','userImg','userRank','userToken']
    list_filter = ['userAccount']
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('userAccount', 'userName')


class CartAdmin(admin.ModelAdmin):
    list_display = ['userAccount','productid','productnum','productprice','isChose','productimg','productname','orderid','isDelete']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('orderid', 'productid','userAccount')


class OrderAdmin(admin.ModelAdmin):
    list_display = ['orderid','userid','progress']

    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = False
    search_fields = ('orderid', 'userid')
admin.site.register(Wheel,WheelAdmin)
admin.site.register(Mustbuy,MustbuyAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Nav,NavAdmin)
admin.site.register(MainShow,MainShowAdmin)
admin.site.register(FoodTypes,FoodTypesAdmin)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)