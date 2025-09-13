# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.__model = model

#     def start_engine(self):
#         return f"The engine of the {self.make} {self.__model} is starting."

# class Car(Vehicle):
#     # def __init__(self):
#     #     self.behaviour = "4 wheels"
#     def start_engine(self):
#         return f"{ self.make}{self.__model} Vroom Vroom!"

# cars = Vehicle("Toyota", "Corolla")
# print(cars.start_engine())
# # bigcars = Car("Honda", "Civic")
# # print(bigcars.start_engine())

# Types of inheritance
# single inheritance
# class Parent:
#     def __init__(self,name):
#         self.name = name
#     def func1(self):
#         print(f"Inside parent class. Name: {self.name}")
# class Child(Parent):
#     def func2(self):
#         print(f"Inside child class. Name: {self.name}")
# object = Child("YoungBoy")
# object.func1()
# object.func2()

# Multi-level inheritance
# class GrandParent:
#     def __init__(self,name):
#         self.name = name
#     def func1(self):
#         print(f"Inside grandparent class. Name: {self.name}")
# class Parent(GrandParent):
#     def func2(self):
#         print(f"Inside parent class. Name: {self.name}")
# class Child(Parent):
#     def func3(self):
#         print(f"Inside child class. Name: {self.name}")
# object = Child("YoungBoy")
# object.func1()
# object.func2()
# object.func3()
# Hierarchical inheritance
# class Parent:
#     def func1(self):
#         print("Inside parent class.")
# class Child1(Parent):
#     def func2(self):
#         print("Inside child1 class.")
# class Child2(Parent):
#     def func3(self):
#         print("Inside child2 class.")
# object1 = Child1()
# object1.func1()
# object1.func2()
# object2 = Child2()
# object2.func1()
# object2.func3()
# Multiple inheritance
# class A:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         print(f"Inside class A. Name: {self.name}")
# class B(A):
#     def greet(self):
#         print(f"Inside class B. Name: {self.name}")
#         super().greet()
# class C(A):
#     def greet(self):
#         print(f"Inside class C. Name: {self.name}")
#         super().greet()
# class D(B,C):
#     def greet(self):
#         print(f"Inside class D. Name: {self.name}")
#         super().greet()
# d = D("YoungBoy")
# d.greet()

# Hybrid inheritance
class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Inside class A. Name: {self.name}")


class B(A):
    def greet(self):
        print(f"Inside class B. Name: {self.name}")
        super().greet()


class C:
    def greet(self):
        print("Inside class C")


class D(B, C):
    def greet(self):
        print(f"Inside class D. Name: {self.name}")
        super().greet()


d = D("youngBoy")
d.greet()
