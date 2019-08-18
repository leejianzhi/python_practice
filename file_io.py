#read a text file then capitilized all characters

fname = input("Enter file name: ")
fh = open(fname)
print(fh.read().upper().strip())

#use forloop

fname = input("Enter file name: ")
fh = open(fname)
for line in fh
    nline = line.rstrip() #remove newline characters
    print(nline.upper())
