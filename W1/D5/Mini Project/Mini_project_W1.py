# Create a TicTacToe game in python, where two users can play together.
# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.



# Tips : Consider the following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!

#Plan of action
#create a game board matrix for tic-tac-toe - DONE
#create players for tic-tac-toe - DONE
#create player score tracker for tic-tac-toe - DONE
#while loop for players turns.
#The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner
#use a loop to check if there is a winner or not
#if all 9 squares are filled there is a tie, then both players will have no points and the total 

# player_1 = 'x'
# player_2 = 'o'
# # player_input(player_1) #To get the position from the player
# # player_input(player_2)  #To get the position from the player

# check_win() #To check whether there is a winner or not.
# winner = check_win()
# tie = check_win()
# display_board() #To display the Tic Tac Toe board
# play() #The main function, which calls all the functions created above


# #which function is the one that should run first? 
# play()
# # starting while loop
# display_board() # game board visualization 

# player_input(player_1)# asking a player to place a move. and update display_board()
# # player identification and x/o placement tracking (and if something is in that place to give an error to the player), 
# check_win()# score/ game tracking vert, horiz, diag for checking a winner or a tie. # restart game if tie.
# player_input(player_2)
# winner = check_win()# print statement for a tie.If there is a winner is it player 1 or player 2? and print statement for who the winner is. # End game if player 1 wiwns, player 2 wins


game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]

def print_board():
    for rows in game:
        print('--|---|--')
        print(" | ".join(rows))
    print("--|---|--")

def reset_board():
    global game
    game = [[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']]

def player_input(player):
    while True:
        try:
            row = int(input(f'Enter Row 1 - 3 for {player}: ')) - 1
            col = int(input(f'Enter Column 1 - 3 for {player}: ')) - 1
            # Adjust the coordinates to the bottom-left start position
            row = 2 - row  # Converts input so that 1 = bottom, 3 = top
            if game[row][col] != ' ':
                print("This spot is taken.")
            else:
                game[row][col] = player
                print_board()
                break
        except (IndexError, ValueError):
            print("Please enter valid row and column numbers between 1 and 3.")

def check_win():
    win_combination = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    players = ['X', 'O']
    for player in players:
        for comb in win_combination:
            counter = 0
            for position in comb:
                if game[position[0]][position[1]] == player:
                    counter += 1
                else:
                    break
            if counter == 3:
                print(f'{player} wins!')
                return True   
    pos_counter = sum(position != ' ' for row in game for position in row)
    if pos_counter == 9:
        print('Tie Game, Play Until Someone Wins!')
        restart = input("Would you like to play again? (y/n): ").strip().lower()
        if restart == 'y':
            reset_board()
            play()
        else:
            print("Thanks for playing!")
        return True

def play():
    while True:
        print_board()
        player_input('X')
        if check_win():
            break
        player_input('O')
        if check_win():
            break
              
play()


  
            



