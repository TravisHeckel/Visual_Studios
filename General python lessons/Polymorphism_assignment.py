
class Player:
    name = "chad"
    username = "zeus"
    password = "123"
    server = "mountain"
    
    def Setup_login(self):
        entry_username = input("Enter your Username: ")
        entry_password = input("Enter your Password: ")
        entry_server = input("Enter the Server you wish to join: ")
        if (entry_server == self.server  and entry_username == self.username and entry_password == self.password):
            print("Identity confirmed, Glad to have you join the game {}!".format(self.name))
        else:
            print("sorry invalid information") 
        
class Forest_Hunters(Player):
    new_username = "ranger"
    party = 4 
    levelMin = 150
    armor = "Sneaky Armor"
    weapons = "dual Daggers"
    
    def Setup_login(self):
        entry_username = input("Enter your Username for the Forest Hunters lobby: ")
        entry_password = input("Enter your Password: ")
        entry_party = input("Enter your Squad: ")
        entry_party = int(entry_party)
        if (entry_party < self.party and entry_new_username == self.username and entry_password == self.password):
            print("Perfect! we have plenty of room for you! Get ready for battle")
        else:
            print("sorry! But either your character information wasn't correct or your party is already full") 

class Raging_Bandits(Player):
    new_username = "sparta"
    party = 8
    king = "Evil Warlock Azilith"
    spell_book = "summoning dead"
    attack = "suprise"
    armor = "none"

    def Setup_login(self):
        entry_username = input("Enter your Username for the Raging Bandits lobby: ")
        entry_password = input("Enter your Password: ")
        entry_party = input("Enter your Squad: ")
        entry_party = int(entry_party)
        if (entry_username == self.new_username and entry_password == self.password and entry_party <= self.party):
            print("Perfect! we have plenty of room for you! Get ready for battle")
        else:
            print("sorry! But either your character information wasn't correct or your party is already full")

    

    

#Player_main=Player()
#Player_main.Setup_login()

Lobby_1=Raging_Bandits()
Lobby_1.Setup_login()

#Lobby_2=Forest_Hunters()
#Lobby_2.Setup_login()
    

    


