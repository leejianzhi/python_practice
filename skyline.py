def myfunc(word):
    result = ""
    index = 0
    for letter in word:
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()
        index += 1
    return result



if __name__ == "__main__":

    myfunc('Anthropomorphism')
