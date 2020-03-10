def unique_list(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)

    print(new_list)




if __name__ == "__main__":

    lst = [1,1,1,1,2,2,3,3,3,3,4,5]
    unique_list(lst)
