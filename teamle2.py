import players
import random

def Teamle(Player):
    #number of years added per guess
    jump = (int)(Player.span/3)
    print()
    print("Try to guess the Top 100 Current NBA Player by their team history. Good Luck!")
    print()
    
    #GUESS 1
    print("Drafted by: " + Player.hist[0] + " in " + Player.years[0])
    print()
    print("Enter your guess: ")
    guess = input()
    if guess == Player.name:
        print()
        print("Congrats!! You must be an NBA fanatic because you Got it in 1! The answer was " + Player.name)
        quit()
    else:
        print()
        print("Incorrect!")
        print()
 
    
    year = 1
    last = 1
    count = 2
    
    #game loop
    for i in range(1, 5):
        print("Next " + str(jump) + " years:")
        while (year < last+jump and year < Player.span):
            print(Player.hist[year] + " in " + Player.years[year])
            year += 1
        last = year
        guess2 = input()
        if guess2 == Player.name:
            print()
            print("Congrats!! You got it in " + str(count) + "! The answer was " + Player.name)
            quit()
        else:
            print()
            print("Incorrect!")
            print()
        count+=1
    
    print("Sorry! The answer was " + Player.name)
        
Teamle(random.choice(players.AllPlayers))
