from game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("q. Quit")
    
    choice = input("Enter your choice: ").lower()
    if choice in ['1', '2', 'q']:
        return choice
    else:
        print("Invalid choice. Please enter 1, 2, or 'q'.")
        return get_user_menu_choice()

def print_results(results):
    print("\nGame Results Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        
        if choice == '1':
            # Play a new game
            game = Game()
            result = game.play()
            # Update results
            results[result] += 1
        elif choice == '2':
            # Show current scores
            print_results(results)
        elif choice == 'q':
            # Quit and print final results
            print_results(results)
            break

# Run the main function
if __name__ == "__main__":
    main()