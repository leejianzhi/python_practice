import sys


def check_input():

    choice = " " #initial choice


    while choice not in range(0,9):
        choice = int(input("Please input a digital number through 1 - 9 to please on the position: "))
        choice = choice - 1

        if choice not in range(0,9):
            print("Invalid input, please enter again.")

    return int(choice)



def user_input(board,choose_player):

    player1_move = ' '
    player2_move = ' '
    print_board = board
#The code logic is not complete,

#there is a improvment that makes display board as a function that will clear up the code a little bit
    if choose_player == 1:
        print("Player1, it is your turn to choose a postion to make a move.")
        position = check_input()
        print("!!!The position is", position)
        player1_move = 'X'
        print("!!!!!The move is",player1_move)
        print_board[position] = player1_move

        print(print_board[0:3])
        print(print_board[3:6])
        print(print_board[6:9])
        who_is_winner(print_board)

    #if player1 has been take a move
    if choose_player:
        print("Player2, it is your turn to choose a postion to make a move.")
        position = check_input()
        player2_move = 'O'
        print_board[position] = player2_move
        print(print_board[0:3])
        print(print_board[3:6])
        print(print_board[6:9])

        who_is_winner(print_board)

    else:
        print('Player1 does not make a move yet.')



def gameon_choice():

    choice = " " #initial choice


    while choice not in ['Y','N']:
        choice = input("Do you want continue play? (Y or N): ")

        if choice not in ['Y','N']:
            print("Invalid input, please enter again.")

    if choice == "Y":
        return True

    else:
        return False

def if_continue():

    choice = input("Please Enter Y to play again or N to exit the game: ")

    if choice == 'Y':
        print('The game will start over again. Thanks for play.')
        user_input(print_board,choice)


    else:
        print('Thanks for your time to play this game.')
        sys.exit()


#check who is the winner
def who_is_winner(gameon_board):

    winner = True

    while winner:

        for i in gameon_board[0:8]: #遍历board
            if gameon_board[0] == gameon_board[1] == gameon_board[2]:
                #This method to print out the winner is not smart
                #needs improve later
                print("Winner is Player with", gameon_board[0])
                if_continue()
                return True
            elif gameon_board[3] == gameon_board[4] == gameon_board[5]:
                print("Winner is Player with", gameon_board[3])
                return True
            elif gameon_board[6] == gameon_board[7] == gameon_board[8]:
                print("Winner is Player with", gameon_board[6])
                return True
            elif gameon_board[0] == gameon_board[3] == gameon_board[6]:
                print("Winner is Player with", gameon_board[0])
                #break
                return True
            elif gameon_board[1] == gameon_board[4] == gameon_board[7]:
                print("Winner is Player with", gameon_board[1])
                return True
            elif gameon_board[2] == gameon_board[5] == gameon_board[8]:
                print("Winner is Player with", gameon_board[2])
                return True
            elif gameon_board[1] == gameon_board[4] == gameon_board[8]:
                print("Winner is Player with", gameon_board[1])
                return True
            elif gameon_board[2] == gameon_board[4] == gameon_board[7]:
                print("Winner is Player with", gameon_board[2])
                return True
            else:
                return False




if __name__ == "__main__":

    user_choice = int(input("Please Enter 1 for Player1(X), Enter 2 for Player2(O): "))
    print('The type of the user choice is: ', user_choice)

    board = ['1','2','3','4','5','6','7','8','9']
    gameon = True


    while gameon:

        user_input(board,user_choice)

        gameon = gameon_choice()
