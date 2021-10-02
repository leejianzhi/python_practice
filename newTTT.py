def user_choice():
    choice = " "

    while choice.isdigit() == False:
        print("\n")
        print("Please input a digit number (Ex. 1,2,3,4,5) \n")
        choice = input("Pleae make a choice, 1 for Player 1(X), and 2 for Player 2(O) to start the game: ")




if __name__ == "__main__":
    user_choice()
