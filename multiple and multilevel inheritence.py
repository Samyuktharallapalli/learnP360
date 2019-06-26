#multilevel inheritance
#base class
class grand_class:
    def firstshow(self):
        print("hello!I am from base class")


class main_class(grand_class):
    def secondshow(self):
        print("Hi!I am from the derived class1")


class first_class(main_class):
    def thirdshow(self):
        print("Hey! I am the derived class2")


p1=first_class()
p1.thirdshow()
p1.secondshow()
p1.thirdshow()

#multiple inheritance


class M_block:
    def show1(self):
        print("I am from 1st parent class")


class F_block:
    def show2(self):
        print("I am from 2nd parent class")


class C_block(M_block,F_block):
    def show3(self):
        print("I am the multiple inherited child block")

f1= C_block()
f1.show3()
f1.show2()
f1.show1()


