import random

def welcome_message():
    print("Welcome to the Adventure Game!")

def get_player_name():
    return input("Please enter your name: ")

def choose_path():
    print("Choose a path:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter the number of your chosen path (1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def handle_path_choice(path_choice, name):
    if path_choice == 1:
        print(f"{name}, you chose the easy path. It's a calm, peaceful trail with no monsters in sight.")
    elif path_choice == 2:
        print(f"{name}, you chose the medium path. The journey is challenging but manageable. There are no monsters here.")
    elif path_choice == 3:
        print(f"{name}, you chose the hard path. Be careful, {name}. You may encounter monsters along the way!")
        result = encounter_monster(name)
        if result == "fail":
            print(f"Game over, {name}.")
            return "fail"

def cross_river():
    depth = float(input("A river blocks your path. How deep is the river (in meters)? "))

    if depth <= 2.0:
        print("The river is shallow. You cross safely.")
    elif 2.0 < depth <= 4.0:
        print("The river is moderately deep. You need to find or build a raft to cross.")
    else:
        print("The river is too deep. You must find another way around.")

def encounter_monster(name):
    print(f"Oh no, {name}! You encountered a monster!")
    action = input("Do you want to fight or run? (fight/run): ").lower()

    if action == "fight":
        if random.choice([True, False]):
            print(f"Well done, {name}! You defeated the monster!")
        else:
            print(f"Sadly, the monster defeated you, {name}.")
            return "fail"
    elif action == "run":
        print(f"You ran away safely, {name}.")
    else:
        print("Invalid choice, the monster attacks while you're confused!")
        return "fail"

def find_treasure(name):
    print(f"As you continue your journey, {name}, you find a treasure chest!")
    guess = int(input("Guess a number to open the chest: "))

    if guess < 5:
        print("You receive a small reward: iron.")
    elif 5 <= guess <= 10:
        print("You receive a medium reward: gold.")
    else:
        print("You receive a large reward: diamond.")

def string_based_decision(name):
    print("What would you like to do next?")
    choice = input("Choose an activity: mining, hunting, or fishing: ").lower()

    if choice == "mining":
        print("You collect 10 gold.")
    elif choice == "hunting":
        print("You collect 5 steaks.")
    elif choice == "fishing":
        print("You collect 5 raw salmon.")
    else:
        print("Invalid activity choice.")

def end_game(name):
    print(f"Congratulations, {name}, you have completed the game!")
    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again == "yes":
        main()
    else:
        print("Thank you for playing!")

def main():
    welcome_message()
    player_name = get_player_name()

    path_choice = choose_path()
    path_result = handle_path_choice(path_choice, player_name)
    if path_result == "fail":
        return

    cross_river()

    find_treasure(player_name)
    string_based_decision(player_name)
    end_game(player_name)

if __name__ == "__main__":
    main()


