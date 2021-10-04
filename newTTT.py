
def check_input():

    choice = " " #initial choice


    while choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input("Please input a digital number through 1 - 10 to please on the position: ")

        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("Invalid input, please enter again.")

    return int(choice)



def user_input(print_board,position):

    user_choice = input("Enter a X or O to make your move: ")

    print_board[position] = user_choice

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
