from enum import Enum
from abc import ABC, abstractclassmethod

class person:
    def __init__(self, weight):
        self.weight = weight
        
class CarStatus(Enum):
    idle = 1
    up = 2
    down = 3

class Car:
    def __init__(self, status: CarStatus):
        self.status = status
        pass 
    
    def move(self):
        pass 

    def stop(self):
        pass        

class Button:
    def __init__(self):
        # self. = 
        pass 
    def pressed(self):
        pass
    def dePressed(self):
        pass
    
class InsideButton(Button):
    def __init__(self, number_buttons):
        nums = [] * number_buttons
        pass 

class OutsideButton(Button):
    def __init__(self):
        nums = [] # 2  

class Display:
    def __init__(self):
        self.Floor = None 
        self.
        
    
class Floor:
    pass 
    
class ElevatorSystem:
    def __init__(self, numFloors, maxCapacity):
        self.numFloors = numFloors
        self.floors = [Floor() for i in range(self.numFloors)]
        self.maxCapacity = maxCapacity 
        
        
    