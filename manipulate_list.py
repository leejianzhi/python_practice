fname = input("Enter file name: ")
fh = open(fname,'r')
lst = list() #list for store data from file
nlst = list() #list for store the data interate from the previously list
for line in fh: #iterate each line from the file
  line = line.rstrip() #remove newline
  lst.append(line) #push data to the list
  lst = line.split(" ") #remove white space
  for i in lst: #iterate each word in the previously list to a new list
    i = i.strip() #remove newlines
    if i not in nlst: #check if the word is unique, if it is then append to the list
      nlst.append(i) #push each word in a new list
      nlst.sort() #sort words in alpha order
print(nlst)
