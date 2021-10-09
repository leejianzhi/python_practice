
def check_input():

    choice = " " #initial choice


    while choice not in range(0,9):
        choice = int(input("Please input a digital number through 1 - 9 to please on the position: "))
        choice = choice - 1

        if choice not in range(0,9):
            print("Invalid input, please enter again.")

    return int(choice)



def user_input(print_board,position):

    player1_choice = ' '
    player2_chocie = ' '

    user_choice = input("Enter a X(Player1) or O(Player2) to make your move: ")

    if user_choice == 'X':
        user_choice = 'X''


        print_board[position] = player1_choice

        print(print_board[0:3])
        print(print_board[3:6])
        print(print_board[6:9])


    else:
        player2_chocie = 'O'
        user_choice = player2_chocie

        print_board[position] = player2_choice

        print(print_board[0:3])
        print(print_board[3:6])
        print(print_board[6:9])



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


if __name__ == "__main__":

    board = ['1','2','3','4','5','6','7','8','9']
    gameon = True

    while gameon:


        position = check_input()

        user_input(board,position)

        gameon = gameon_choice()
