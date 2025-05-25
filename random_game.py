import random

def play_game():
    print("Welcome to the Random Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    # Game loop
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"\nAttempt {attempts+1}/{max_attempts}. Enter your guess: "))
            
            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            attempts += 1
            
            # Check guess
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
                return
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # If loop completes without a correct guess
    print(f"\nGame over! You've used all {max_attempts} attempts.")
    print(f"The secret number was {secret_number}.")

if __name__ == "__main__":
    play_game()
    
    # Ask if player wants to play again
    while True:
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            play_game()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")