class str_demo:

    s = "类变量" # 类变量  类加载到内存中就会被创建   类被销毁时，同步被销毁

    def test(self):
        print("父类")

    def replace(self):
        self.a = "实例变量" # 实例变量 调用该变量创建的实例方法时 对象被销毁时同步被销毁掉
        b = "局部变量"  # 局部变量  方法运行结束就被销毁
        print("字符串替换")

    def split(self):
        print(str_demo.s) # 访问类变量
        print(__class__.s) # 访问类变量(推荐)
        print(self.s) # 不推荐
        print(self.a) # 访问实例变量

# sd = str_demo() # 实例化 sd就是一个对象
# sd.s = "hello"
# print(sd.s)



class Test1:
    def __init__(self, initval = None, name = 'var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, objtype):
        print("Get内置方法",self.name)
        return self.val
    def __set__(self, obj, val):
        print("updating",self.name)
        self.val = val
class myClass:
    x = Test1(10,'var "x"')
    y = 5

# t = Test1(10,'var "x"')
# print(t)
#
# m = myClass()
# print(m.x)
# m.x = 20
# print(m.x)
# print(m.y)


# class A(str_demo):
#     def test(self):
#         print("子类")
#     a = 10
#
# hhh = A()
# hhh.test()



class Product():

    # def __init__(self,name,quantity,price):
    #     self.name = name
    #     if quantity<0:
    #         raise ValueError('quantity must be >= 0')
    #     self.quantity = quantity
    #     if price<0:
    #         raise ValueError('price must be >= 0')
    #     self.price = price

    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self,value):
        if value<0:
            raise ValueError('quantity must be >= 0')
        else:
            self._quantity = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price must be >= 0')
        else:
            self._price = value

Product("电脑",1,100)