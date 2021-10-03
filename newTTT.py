def check_input():

    choice = " "


    while choice not in ['0','1','2','3','4','5','6','7','8','9']:
        choice = input("Please input a digital number through 1 - 10 to please on the position: ")
        print_board(choice)

        if choice not in ['0','1','2','3','4','5','6','7','8','9']:
            print("Invalid input, please enter again.")


def print_board(choice):

    line_1 = ['0','1','2']
    line_2 = ['3','4','5']
    line_3 = ['6','7','8']

    print(line_1)
    print(line_2)
    print(line_3)

    if(choice == 0):
        choice = line_1[0]

    print(line_1)
    print(line_2)
    print(line_3)




if __name__ == "__main__":
    check_input()
