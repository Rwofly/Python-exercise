#构建一个汽车类
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0 #给属性指定默认值，odometer_reading指里程读数。

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):#通过方法改变属性odometer_reading的值
        self.odometer_reading=mileage

    def increment_odometer(self,miles):
        if miles>0:
            self.odometer_reading+=miles
        else:
            print("You can't roll back an odometer")

my_new_car=Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())#调用方法
my_new_car.read_odometer()#调用方法

my_new_car.odometer_reading=23 #直接修改属性的值
print(my_new_car.get_descriptive_name())#调用方法
my_new_car.read_odometer() #调用方法，属性read_odometer发生改变

my_new_car.update_odometer(33)#调用方法，改变odometer_reading的值
print(my_new_car.get_descriptive_name())#调用方法
my_new_car.read_odometer()#调用方法

my_new_car.increment_odometer(12)#通过方法增加属性odometer_reading
print(my_new_car.get_descriptive_name())#调用方法
my_new_car.read_odometer()#调用方法

my_new_car.increment_odometer(-10)#尝试增加负数
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

