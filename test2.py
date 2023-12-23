# A program to read the value from private method 
class Javatpoint:
    def __init__(self, year=27):
        self._year = year

    @property
    def Aboutyear(self):
        return self.__year

    @Aboutyear.setter
    def Aboutyear(self, x):
        self.__year = x


grad_obj = Javatpoint()
print(grad_obj._year)

grad_obj.year = 2020
print(grad_obj.year)