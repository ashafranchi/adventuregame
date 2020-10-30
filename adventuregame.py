print("Welcome to Wonderland, A Taylor Swift Adventure!")

name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 13

if age >= 8:
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with 13 points! Let's play!")
    if wants_to_play == "no":
        print("See ya!")
    
    nineteen_or_reputation = input("First choice...Are you Ready for It? Pick one: 1989 or Reputation? ").lower()
    if nineteen_or_reputation == "1989":
        ans = input("Cute! Will you go Into the Woods or be Welcomed to New York? (woods/nyc)").lower()
        if ans == "woods":
            print("The world may be black and white, but you are in screaming color. You win 4 points.")
            health += 4
        elif ans == "nyc":
            print("The lights are too bright and it's hard to see! You lose 5 points.")
            health -= 5
        ans = input("Trivia Question: What type of animal does Taylor Swift love? ").lower()
        if ans == "cats":
            health += 3
            print("Purrr! You got it right!")
        else:
            health -= 8
            print("The correct answer is cats. You lose 8 points.")

            if health <= 0:
                print("You have", health, "points. You are escorted out of Wonderland. We are sorry your time is up here, what a Sad Beautiful Tragic ending. Bye Swiftie!")
            else:
                print("You have won the game with", health, "points! You are quite the Lucky One. We hope you have enjoyed Wonderland. Bye Swiftie!")
    else:
        "Bye!"
    if nineteen_or_reputation == "reputation":
        ans = input("You are so cool! You gain 1 point. Are you hopping into a Getaway Car or are you going shopping for a Dress? (Car/Dress) ").lower()
        health +=1
        if ans == "car":
            print("You put the money in the bag and stole the keys. You win 7 points.")
            health += 7
        elif ans == "dress":
            print("You look Gorgeous, but dresses cost money. You lose 5 points.")
            health -= 5

        ans = input("Trivia Question: What type of animal does Taylor Swift love? ").lower()
        if ans == "cats":
            health += 3
            print("Purrr! You got it right!")
        else:
            health -= 9
            print("The correct answer is cats. You lose 9 points.")

        if health <= 0:
            print("You have", health, "points. You are escorted out of Wonderland. We are sorry your time is up here, what a Sad Beautiful Tragic ending.")
        else:
            print("You have won the game with", health, "points! You are quite the Lucky One. We hope you have enjoyed Wonderland.")
    else: print("Bye Swiftie!")
                
else:
    print ("You might be too young to play this game.")