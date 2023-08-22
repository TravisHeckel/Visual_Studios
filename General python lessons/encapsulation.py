import random

luck = random.randrange(1,10)
diamonds = 1
Rubies = 1

class checkJewels:
    def __init__(self):
        self.__diamond = diamonds
        self._Ruby = Rubies

        if self.__diamond == 1 and  self._Ruby == 1:
            print ("My Jewels are safe!")
        else:
            print("Oh no I lost my Jewels!")



class safe:
    def state(self):
        self._alarm = False
        i = luck
        if i > 5:
            rubies = 0
            print ("HE GOT THE RUBY!")
            self._alarm = True
        elif i > 9:
            diamonds = 0
            rubies = 0
            print ("HE GOT THE DIAMOND AND RUBY!")
        else:
            print ("HE COULDN'T GET ANYTHING")
            self._alarm = True



class thief:
          
    def running(self):
        self.__speed = True
        i = luck
        if i < 5:
            self.__speed = True
        else:
            self.__speed = False
        
        if self.__speed == True:
            print ("He got away!")
        else:
            print ("He got caught!")

        
        
treasure = checkJewels()
heist = safe()
heist.state()
robber = thief()
robber.running()
treasure = checkJewels()



        

