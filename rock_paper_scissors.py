import random

# Valid choices
choices = ['rock', 'paper', 'scissors']

# Score counters
player_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors!")
print("Type 'exit' anytime to quit.\n")

while True:
    # Get user input
    user_choice = input("Enter rock, paper or scissors: ").lower()

    # Exit condition
    if user_choice == 'exit':
        print("\n👋 Thanks for playing!")
        print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
        break

    # Validate input
    if user_choice not in choices:
        print("❌ Invalid input! Please type 'rock', 'paper', or 'scissors'.\n")
        continue

    # Get computer choice
    computer_choice = random.choice(choices)
    print(f"💻 Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("✅ You win this round!")
        player_score += 1
    else:
        print("💻 Computer wins this round!")
        computer_score += 1

    # Show current score
    print(f"🏆 Score -> You: {player_score} | Computer: {computer_score}\n")
