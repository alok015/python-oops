class Vehicle:

    def __init__(self,color,maxSpeed):
        self.color = color
        self._maxSpeed = maxSpeed

    def getMaxSpeed(self):
        return self.__maxSpeed
    def setMaxSpeed(self,maxSpeed):
        self.__maxSpeed = maxSpeed

    def print(self):
        print('color :',self.color)
        print('maxSpeed is ',self.__maxSpeed)
class Car(Vehicle):

    def __init__(self,color,maxSpeed,numGears,isConvertible):

        super().__init__(color,maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible

    def print(self):
        # self.print()
        print('Numgears: ',self.numGears)
        print('Isconvertible:',self.isConvertible)

    def substract(self):
        pass

# c = Car("red",15,3,False)
# c.print()
v = Vehicle('red',18)
print(v._maxSpeed)
v._maxSpeed = 30
print(v._maxSpeed)

# c2 = Vehicle("blue",15)
# c2.print()

