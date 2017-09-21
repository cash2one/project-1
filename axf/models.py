from django.db import models

# Create your models here.

class Wheel(models.Model):
    img = models.CharField(u'图片路径',max_length=150)
    name = models.CharField(u'名称',max_length=20)
    trackid = models.CharField(u'id',max_length=20)

class Nav(models.Model):
    img = models.CharField(u'图片路径',max_length=150)
    name = models.CharField(u'名称',max_length=20)
    trackid = models.CharField(u'id',max_length=20)

class Mustbuy(models.Model):
    img = models.CharField(u'图片路径',max_length=150)
    name = models.CharField(u'名称',max_length=20)
    trackid = models.CharField(u'id',max_length=20)

class Shop(models.Model):
    img = models.CharField(u'图片路径',max_length=150)
    name = models.CharField(u'名称',max_length=20)
    trackid = models.CharField(u'id',max_length=20)



class MainShow(models.Model):
    trackid = models.CharField(u'id',max_length=10)
    name = models.CharField(u'名称',max_length=20)
    img = models.CharField(u'图片路径',max_length=100)
    categoryid = models.CharField(u'类别',max_length=10)
    brandname = models.CharField(u'商标',max_length=20)

    img1 = models.CharField(u'1-图片路径',max_length=100)
    childcid1 = models.CharField(u'1-子类id',max_length=10)
    productid1 = models.CharField(u'1-商品id',max_length=10)
    longname1 = models.CharField(u'1-介绍',max_length=50)
    price1 = models.CharField(u'1-价格',max_length=10)
    marketprice1 = models.CharField(u'1-市场价',max_length=10)

    img2 = models.CharField(u'2-图片路径2',max_length=100)
    childcid2 = models.CharField(u'2-子类id',max_length=10)
    productid2 = models.CharField(u'2-商品id',max_length=10)
    longname2 = models.CharField(u'2-介绍',max_length=50)
    price2 = models.CharField(u'2-价格',max_length=10)
    marketprice2 = models.CharField(u'2-市场价',max_length=10)

    img3 = models.CharField(u'3-图片路径2',max_length=100)
    childcid3 = models.CharField(u'3-子类id',max_length=10)
    productid3 = models.CharField(u'3-商品id',max_length=10)
    longname3 = models.CharField(u'3-介绍',max_length=50)
    price3 = models.CharField(u'3-价格',max_length=10)
    marketprice3 = models.CharField(u'3-市场价',max_length=10)


# 分类模型
class FoodTypes(models.Model):
    typeid = models.CharField(u'id',max_length=10)
    typename = models.CharField(u'类型名',max_length=20)
    typesort = models.IntegerField(u'排序等级',)
    childtypenames = models.CharField(u'全部分类',max_length=150)
# 商品模型类
class Goods(models.Model):
    # 商品id
    productid = models.CharField(u'商品id',max_length=10)
    # 商品图片
    productimg = models.CharField(u'商品图片',max_length=150)
    # 商品名称
    productname = models.CharField(u'商品名称',max_length=50)
    # 商品长名称
    productlongname = models.CharField(u'商品长名称',max_length=100)
    # 是否精选
    isxf = models.NullBooleanField(u'是否精选',default=False)
    # 是否买一赠一
    pmdesc = models.CharField(u'是否买一赠一',max_length=10)
    # 规格
    specifics = models.CharField(u'规格',max_length=20)
    # 价格
    price = models.DecimalField(u'价格',max_digits=10, decimal_places=6)
    # 超市价格
    marketprice = models.DecimalField(u'超市价格',max_digits=10, decimal_places=6)
    categoryid = models.CharField(u'类别id',max_length=10)
    # 子类组id
    childcid = models.CharField(u'子类组id',max_length=10)
    # 子类组名称
    childcidname = models.CharField(u'子类组名称',max_length=10)
    # 详情页id
    dealerid = models.CharField(u'详情页id',max_length=10)
    # 库存
    storenums = models.IntegerField(u'库存',)
    # 销量
    productnum = models.IntegerField(u'销量',)



# 用户模型类
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(u'用户名',max_length=20,unique=True)
    #
    userPasswd  = models.CharField(u'密码',max_length=20)
    # 昵称
    userName    =  models.CharField(u'昵称',max_length=20)
    # 手机号
    userPhone   = models.CharField(u'手机号',max_length=20)
    # 地址
    userAdderss = models.CharField(u'地址',max_length=100)
    # 头像路径
    userImg     = models.CharField(u'头像路径',max_length=150)
    # 等级
    userRank    = models.IntegerField(u'等级',)
    # touken验证值，每次登陆之后都会更新
    userToken   = models.CharField(u'touken验证值',max_length=50)
    @classmethod
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u


class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)
class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)
class Cart(models.Model):
    userAccount = models.CharField(u'用户名',max_length=20)
    productid = models.CharField(u'商品id',max_length=10)
    productnum = models.IntegerField(u'数量',)
    productprice = models.CharField(u'总价',max_length=10)
    isChose = models.BooleanField(u'是否勾选',default=True)
    productimg = models.CharField(u'图片路径',max_length=150)
    productname = models.CharField(u'商品名称',max_length=100)
    orderid = models.CharField(u'订单号',max_length=20,default="0")
    isDelete = models.BooleanField(u'逻辑删除',default=False)
    objects = CartManager1()
    obj2 = CartManager2()
    @classmethod
    def createcart(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c = cls(userAccount = userAccount,productid = productid,productnum=productnum,productprice=productprice,isChose=isChose,productimg=productimg,productname=productname,isDelete=isDelete)
        return c




class Order(models.Model):
    orderid = models.CharField(u'订单号',max_length=20)
    userid  = models.CharField(u'用户id',max_length=20)
    progress = models.IntegerField(u'订单进度',)

    @classmethod
    def createorder(cls, orderid, userid, progress):
        o = cls(orderid=orderid, userid=userid, progress=progress)
        return o