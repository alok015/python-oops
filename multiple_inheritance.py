class Mother:

    def __init__(self):
        self.name = 'Manju'
        super().__init__()

    def print(self):
        print('Print of mother called')

class Father:

    def __init__(self):
        self.name = 'Ajay'

    def print(self):
        print('Print of father called')

class Child(Mother,Father):

    def __init__(self):
        super().__init__()

    def printChild(self):
        print('Name of child is ', self.name)

c = Child()
c.printChild()

print(Child.mro())