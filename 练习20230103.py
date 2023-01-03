#类的练习
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over")

my_dog=Dog('Huang',19)
my_dog.sit()
my_dog.roll_over()
my_dog2=Dog('Hello',12)
my_dog2.sit()
my_dog2.roll_over()
