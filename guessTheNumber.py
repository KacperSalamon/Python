import random

randomNumber = random.randint(1,10)

yourName = input("Hello please provide your name: ")
chance = 0

print("Thank you so much to join my game {}. You have to guess the number beetwen 1 & 10. I think this will be simple for you. Your chance to guess = 3".format(yourName))

while chance < 3:
    guess = int(input("Your {} chance: ".format(chance + 1)))
    chance += 1
    
    if guess < randomNumber :
        print("Your number is too low, sorry - try again")
    
    if guess > randomNumber:
        print("Your number is to hight, sorry - try again")
    if guess == randomNumber:
        break
if guess == randomNumber:
    print("Congratulations {} - you win in {} chance!!!".format(yourName, chance, randomNumber))
else:
    print("Sorry you lost all of yours chance - the number which you should find is {}:(".format(randomNumber)) 
