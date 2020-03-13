def palindrome(s):
    halfStr = len(s)//2
    base = -1
    resultTrue = 0
    resultFalse = 0

    for i in range(0,len(s)//2):

        if s[i] == s[base - i] :

            resultTrue += 1

        else:
            resultFalse += 1

    if resultTrue == len(s)//2:
        print('True')

    else:
        print('False')





if __name__ == "__main__":

    str = 'helleh'
    palindrome(str)
