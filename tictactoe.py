"""
Welcome to Tic Tac Toe!
Please input an answer:
An answer of "!STARTAI" will play against the computer.
An answer of "!START2P" will start a game for two players.
An answer of "!QUIT" will quit the game.
"""
#Version 0.2
#TODO:
#split game logic from input-output logic
#Add a gamestate class that allows for simplification
#Get rid of if/else blocks and instead use a tuple with dictionary or
#board = do_move(board, "X", (1, 1))
def draw_board(board):
    print()
    print((" %s | %s | %s ") % (board[0][0], board[0][1], board[0][2]))
    print("-----------")
    print((" %s | %s | %s ") % (board[1][0], board[1][1], board[1][2]))
    print("-----------")
    print((" %s | %s | %s ") % (board[2][0], board[2][1], board[2][2]))
    print()
def draw_helper_board():
    print()
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("Type in a number above to select your move!")
def game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                return "X"
            else:
                return "O"
        elif board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return "X"
            else:
                return "O"
        elif board[0][0] == board[1][1] == board[2][2]:
            if board[1][1] == "X":
                return "X"
            else:
                return "O"
        elif board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] == "X":
                return "X"
            else:
                return "O"
    return False
def START_AI():
    print("Computer AI is being worked on!")
def START_2P():
    board_state = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #While player_turn is True, it is player 1's turn.
    #While player_turn is False, it is player 2's turn.
    player_turn = True
    draw_helper_board()
    while not game_over(board_state):
        if player_turn:
            print("Player 1, what is your move?")
            player_1_input = int(input("...>"))
            player_turn = False
            if player_1_input == 1:
                board_state[0][0] = "X"
            elif player_1_input == 2:
                board_state[0][1] = "X"
            elif player_1_input == 3:
                board_state[0][2] = "X"
            elif player_1_input == 4:
                board_state[1][0] = "X"
            elif player_1_input == 5:
                board_state[1][1] = "X"
            elif player_1_input == 6:
                board_state[1][2] = "X"
            elif player_1_input == 7:
                board_state[2][0] = "X"
            elif player_1_input == 8:
                board_state[2][1] = "X"
            elif player_1_input == 9:
                board_state[2][2] = "X"
            draw_board(board_state)
        else:
            print("Player 2, what is your move?")
            player_2_input = int(input("...>"))
            player_turn = True
            if player_2_input == 1:
                board_state[0][0] = "O"
            elif player_2_input == 2:
                board_state[0][1] = "O"
            elif player_2_input == 3:
                board_state[0][2] = "O"
            elif player_2_input == 4:
                board_state[1][0] = "O"
            elif player_2_input == 5:
                board_state[1][1] = "O"
            elif player_2_input == 6:
                board_state[1][2] = "O"
            elif player_2_input == 7:
                board_state[2][0] = "O"
            elif player_2_input == 8:
                board_state[2][1] = "O"
            elif player_2_input == 9:
                board_state[2][2] = "O"
            draw_board(board_state)
    print(("%s wins!") % (game_over(board_state)))
    
def welcome():
    #__doc__ is the header in triple quotes 'Welcome to Tic Tac Toe!...'
    print (__doc__)
def main():
    done = False
    #This while loop ensures that we keep stay in the menu as
    #long as we are not done playing!
    while not done:
        welcome()
        answer = input("What is your answer?\n...>")
        if answer.upper() == "!STARTAI":
            START_AI()
        if answer.upper() == "!START2P":
            START_2P()
        if answer.upper() == "!QUIT":
            break
    print ("Thanks for trying TIC TAC TOE! Goodbye!")
    
            

##best practice, see
##http://stackoverflow.com/questions/419163/what-does-if-name-main-do
##for details
if __name__ == "__main__":
    main()
