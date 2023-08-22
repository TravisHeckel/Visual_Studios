import sqlite3

#data to be added to our table
examples = (('Jean-Baptiste Zorg', 'Human', 122),('Korben Dallas', 'Meat Popsicle', 100), ("Ak\'not", 'Mangalore', -5)) 

with sqlite3.connect('RAM.db') as connection:
    c = connection.cursor()
    #We created the table Roster already
##    c.execute ("CREATE TABLE Roster (Name TEXT, Species TEXT, IQ INT)")
    #We inserted data into the table already
##    c.executemany ("INSERT INTO Roster VALUES(?, ?, ?)",examples)
    #We updated one of our values
##    c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    c.execute("SELECT Name, IQ FROM ROster WHERE Species = 'Human'")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
