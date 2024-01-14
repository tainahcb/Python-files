"""
Author: Tainah Correia Barreto
"""
# To pass this stage, you must read Alma 17-27 in the Book of Mormon.
# All questions will deal with the people of Ammon and their conversion.
# Be aware that there are some trick questions.

print("Welcome to the game of the Anti-Nephi-Lehies!")
print('You are in the Sons of Mosiah Phase.\nTo pass this stage, you must answer some questions about the preaching\nof the Sons of Mosiah among the Lamanites.')
print()
print("You are in a distant land.")

response1 = input("Do you want to follow the path of peace or the path of war? (PEACE / WAR)")

if response1.lower() == "peace":
    print("You chose the path of peace.")
    response2 = input("Do you want to help the Anti-Nephi-Lehies or join the Lamanites? (HELP / JOIN)")

    if response2.lower() == "help":
        print("You decide to help the Anti-Nephi-Lehies.")
        response3 = input("Do you want to preach the gospel or build a city? (PREACH / BUILD)")

        if response3.lower() == "preach":
            print("You preach the gospel and many people convert.")
            print("Congratulations, you win the game!")

        elif response3.lower() == "build":
            print("You build a prosperous city for the Anti-Nephi-Lehies.")
            print("Congratulations, you win the game!")

    elif response2.lower() == "join":
        print("You decide to join the Lamanites.")
        response4 = input("Do you want to fight against the Anti-Nephi-Lehies or repent? (FIGHT / REPENT)")

        if response4.lower() == "fight":
            print("You fight against the Anti-Nephi-Lehies and lose the battle.")
            print("Unfortunately, you lose the game.")

        elif response4.lower() == "repent":
            print("You repent and abandon the war.")
            print("Congratulations, you win the game!")

elif response1.lower() == "war":
    print("You chose the path of war.")
    response5 = input("Do you want to lead the Lamanites or join the Nephites? (LEAD / JOIN)")

    if response5.lower() == "lead":
        print("You become a powerful leader of the Lamanites.")
        response6 = input("Do you want to conquer territories or make a peace treaty? (CONQUER / TREATY)")

        if response6.lower() == "conquer":
            print("You conquer many territories, but the war continues.")
            print("Unfortunately, you lose the game.")

        elif response6.lower() == "treaty":
            print("You make a peace treaty and end the war.")
            print("Congratulations, you win the game!")

    elif response5.lower() == "join":
        print("You decide to join the Nephites.")
        response7 = input("Do you want to fight for freedom or betray the Nephites? (FIGHT / BETRAY)")

        if response7.lower() == "fight":
            print("You fight for freedom and help the Nephites win the war.")
            print("Congratulations, you win the game!")

        elif response7.lower() == "betray":
            print("You betray the Nephites and are defeated.")
            print("Unfortunately, you lose the game.")

print("Thank you for playing!")
