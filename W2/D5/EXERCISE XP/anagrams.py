from anagram_checker import Anagram_Checker

class Menu(Anagram_Checker):
    def __init__(self):
        self.anagram_checker = Anagram_Checker()
        self.run_menu()

    def run_menu(self):
        while True:
            print("\nWelcome to the Anagram Checker!")
            print("1. Input a word to find its anagrams")
            print("2. Exit")
            choice = input("Please select an option (1 or 2): ")
            if choice == '1':
                self.input_word()
            elif choice == '2':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def input_word(self):
        user_word = input("Enter a word: ").strip()
        
        # Validate input
        if not user_word.isalpha():
            print("Error: Only alphabetic characters are allowed. Please try again.")
            return
        
        if ' ' in user_word:
            print("Error: Please enter only a single word.")
            return

        # Get anagrams and display results
        user_word = user_word.lower()
        anagrams = self.anagram_checker.get_anagram(user_word)
        
        if anagrams:
            print(f"\nWord: {user_word.capitalize()}")
            print("Anagrams found:", ", ".join(anagrams))
        else:
            print(f"\nNo anagrams found for '{user_word}'.")
Menu()
