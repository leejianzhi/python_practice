import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_245351.txt"
handle = open(name)

new_list = []
sum = 0

for line in handle:

    y = re.findall('[0-9]+',line)
    #sum = sum + y
    for i in y:
        new_list.append(i)
#print(len(new_list))

for ele in range(0, len(new_list)):
    sum = sum + int(new_list[ele])
print(sum)
