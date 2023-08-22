from abc import ABC, abstractmethod
class Animal(ABC):
    
    def size(self, i):
        if i == 1:
            print("they are small sized")
        elif i == 2:
            print("they are medium sized")
        else:
            print("they are large sized")
        
    @abstractmethod
    def movement(self):
        pass
 
class Human(Animal):
    i = 2
    def movement(self):
        print("Humans can walk")
 
class Snake(Animal):
    i = 1 
    def movement(self):
        print("Snakes can slither")
 
class Frog(Animal):
    i = 1
    def movement(self):
        print("Frogs can jump")
 
class Cheeta(Animal):
    i = 2
    def movement(self):
        print("Cheetas can run")
         
# Driver code
R = Human()
R.movement()
R.size(2)

K = Snake()
K.movement()
K.size(1)

R = Frog()
R.movement()
R.size(1)

K = Cheeta()
K.movement()
K.size(2)
