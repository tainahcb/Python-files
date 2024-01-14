"""
Author: Tainah Correia Barreto
"""
print("Welcome to the game!")
print("You are in a dark forest.")

answer1 = input("Do you want to go left or right? (LEFT / RIGHT)")

if answer1 == "LEFT":
    print("You have found an abandoned hut.")
    answer2 = input("Do you want to enter the hut or continue walking? (ENTER / WALK)")
    if answer2 == "ENTER":
        print("Inside the hut, you'll find a treasure!")
        print("Congratulations, you've won the game!")
    elif answer2 == "WALK":
        print("You're still walking through the forest.")
        answer3 = input("Do you want to climb a tree or swim in the river? (TREE / RIVER)")
        if answer3 == "TREE":
            print("You climb a tall tree and see a clearing in the distance.")
            print("Unfortunately, you slipped and fell and lost the game.")

        elif answer3 == "RIVER":
            print("You swim the river and find a secret passage.")
            print("Congratulations, you've won the game!")

elif answer1 == "RIGHT":
    print("You find a narrow path.")
    answer4 = input("Do you want to go forward or back? (FORWARD / BACK)")

    if answer4 == "FORWARD":
        print("You go straight ahead and come across a lake.")
        answer5 = input("Do you want to swim in the lake or fish? (SWIM / FISH)")

        if answer5 == "SWIM":
            print("You swim in the lake and are attacked by a sea monster.")
            print("Unfortunately, you've lost the game.")

        elif answer5 == "FISH":
            print("You caught a giant fish!")
            print("Congratulations, you've won the game!")

    elif answer4 == "BACK":
        print("You return home and finish the game.")

print("Thanks for playing!")