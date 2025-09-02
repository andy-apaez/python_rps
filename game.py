import random

# ASCII art
art = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

def play():
    options = ["rock", "paper", "scissors"]

    print("Welcome to Rock-Paper-Scissors! 🎮")
    rounds = int(input("Play best of (3, 5, 7)? Enter a number: "))

    user_score = 0
    computer_score = 0
    winning_score = (rounds // 2) + 1

    while user_score < winning_score and computer_score < winning_score:
        user_choice = input("\nEnter rock, paper, or scissors: ").lower()

        if user_choice not in options:
            print("Invalid choice. Try again!")
            continue

        computer_choice = random.choice(options)

        # Show ASCII art
        print(f"\nYou chose {user_choice}: {art[user_choice]}")
        print(f"Computer chose {computer_choice}: {art[computer_choice]}")

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 😢")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

    print("\n🏆 Final Result 🏆")
    if user_score > computer_score:
        print("🎉 You are the CHAMPION!")

    else:
        print("💻 Computer is the CHAMPION!")
       

# Run game
play()
