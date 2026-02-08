from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


# Child Class 1
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started with key ignition ")


# Child Class 2
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started with self-start ")


# Child Class 3
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started with heavy-duty ignition ")


# Creating Objects
v1 = Car()
v2 = Bike()
v3 = Bus()

# Calling start_engine()
v1.start_engine()
v2.start_engine()
v3.start_engine()
