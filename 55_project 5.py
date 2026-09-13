import random

def play_game():
    print("--- Snake  Water  Gun Game ---")
    print("Choose one: 's' for Snake, 'w' for Water, 'g' for Gun")
    
    # 1. user se input lena hai
    user_choice = input("Your choice: ").lower()
    
    # 2. computer random choice
    options = ['s', 'w', 'g']
    computer_choice = random.choice(options)
    
    # dictionary for given full name to choice
    names = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
    
    # input validation
    if user_choice not in options:
        print("Invalid choice! Please choose s, w, or g.")
        return

    print(f"\nYou chose: {names[user_choice]}")
    print(f"Computer chose: {names[computer_choice]}\n")

    # 3. game logics (If-Else Rules)
    if user_choice == computer_choice:
        print(" It's a Tie (match draw)!")
    elif (user_choice == 's' and computer_choice == 'w') or \
         (user_choice == 'w' and computer_choice == 'g') or \
         (user_choice == 'g' and computer_choice == 's'):
        print(" You Win ! kartik Bhai is proud of you! ")
    else:
        print(" Computer Wins ! Try again.")

# function call for game run
play_game()