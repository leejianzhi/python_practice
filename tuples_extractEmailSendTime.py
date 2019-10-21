name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith("From") and not line.startswith("From:"):
        words = line.split()
        	#print(words[5][0:2])

        counts[words[5][0:2]] = counts.get(words[5][0:2],0) + 1

lst = counts.items()
#print(val, key)

#print(lst)

lst = sorted(lst)
for key, val in lst:
    print(key, val)
