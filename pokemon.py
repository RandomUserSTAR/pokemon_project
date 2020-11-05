import sys
import random

def play():
    while True:
        p_choice = str(input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur'"))
        if p_choice == '1':
            p_choice = 'Charmander'
        elif p_choice == '2':
            p_choice = 'Squirtle'
        elif p_choice == '3':
            p_choice = 'Bulbasur'
# Part for A.I
        cpu_random = random.randint(1,3)
        if cpu_random == 1:
            cpu_choice = 'Charmander'
        elif cpu_random == 2:
            cpu_choice = 'Squirtle'
        elif cpu_random == 3:
            cpu_choice = 'Bulbasur'




        def battle():

            if p_choice == cpu_choice:
                print(f"{p_choice} and {cpu_choice} have the same power so they started to mingle about thier powers")
                sys.exit()


            elif p_choice == 'Charmander' and cpu_choice == 'Squirtle':
                print(f"The Computer Wins! and the player has {p_choice} and cpu has {cpu_choice}")
                sys.exit()
            elif p_choice == 'Squirtle' and cpu_choice == 'Charmander':
                print(f"The Player Wins! and the player has {p_choice} and cpu has {cpu_choice}")
                sys.exit()


            elif p_choice == "Squirtle" and cpu_choice == 'Bulbasur':
                print(f"The Computer Wins! and the player has {p_choice} and cpu has {cpu_choice}")
                sys.exit()
            elif p_choice == 'Bulbasur' and cpu_choice == 'Squirtle':
                print(f"The Player Wins! and the player has {p_choice} and cpu has {cpu_choice}")
                sys.exit()


            elif p_choice == 'Bulbasur' and cpu_choice == 'Charmander':
                print(f"The Computer Wins! and the player has {p_choice} and cpu has {cpu_choice}")
                sys.exit()
            elif p_choice == 'Charmander' and cpu_choice == 'Bulbasur':
                print(f"The Player Wins! and the player has {p_choice} and cpu has {cpu_choice}")
                sys.exit()

        battle()




def start_game():
    while True:
        begin = input("Would you like to play pokemon(y/n): ")
        if begin == 'y':
            play()
            return begin
        while begin != 'y':
            if begin == 'n':
                print("Game Over")
                return begin
            else:
                print('Please try again')
                break

start_game()
