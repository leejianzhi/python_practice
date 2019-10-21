name = input("Enter file:")
#if input zero line then the default file name will be as below
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

#the file content is like a log of email server
#this python application will find the sender who
#send the most emails according to that text file

for line in handle:
    word = line.split()
    if line.startswith("From:"):
    	counts[word[1]] = counts.get(word[1],0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)
