
from abc import ABC,abstractmethod
from Rectangle import *
from Circle import *

class Shape(ABC):
    def __init__(self,height,width,radius):
      self.height=height
      self.width=width
      self.radius=radius

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


circle= Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle= Rectangle(10,20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())