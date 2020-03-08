class PartyAnimal:
    x = 0

    def __init__(self): #pass self when that is constructed
        print('This is the constructed')

    def party(self):
        self.x = self.x + 1 #self.x = an.x when call the oo
        #each time call the class that will add 1
        #self.x start with zero. When call the class that 1 will goes to
        #x and next time x (x=1) will add 1 and 2 will assign to x
        print("So far", self.x)

    def __del__(self): #print current value when destructed finished
        print('This is the destructed', self.x)
print(self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()
an = 42
print('an contains', an)
