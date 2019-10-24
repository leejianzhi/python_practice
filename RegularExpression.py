#Regular Expressions

# ^X.*: . -> Any character *--> Zero or more times ^--> Start with

import re


print("Test case 1 start\n")

x = 'My 2 favorite number are 19 and 42'
y = re.findall('[0-9]+', x) # 0 - 9 one or more digits
print(y) #return a list of all possbile matches
print("\n")
print("Test case 1 end \n")

print("Test case 2 start\n")

y = re.findall('[AIOU]+',x) #there is no AIOU in the string
print(y)
print("\n")
print("Test case 2 end \n")

#Greedy Matching..return Largest mathes string
print("Test case 3 start\n")

x = 'From: Using the: character'
y =re.findall('^F.+:.',x)
print(y)

print("\n")
print("Test case 3 end \n")

#Non-Greedy Matching -- shortest

print("Test case 4 start\n")

x = 'From: Using the : character'
y = re.findall('^F.+?:', x) # '?' last character in the match is a ':'
print(y)                  # the output will be the 'From:' only

print("\n")
print("Test case 4 end \n")

print("Test case 5 start\n")

x = 'From leejianzhi@lee.com sat jan 5 09:14:16 2019'
y = re.findall('\S+@\S+',x) #!!!!! Regular Expressions is case sensitive
print(y) # The '\S+@\S+' The '\S' is mean non-whitespace character
# '\S+@\S+' means at least one non-whitespace character
print("\n")
print("Test case 5 end \n")

print("Test case 6 start\n") #same as test case 5 but different method

x = 'From leejianzhi@lee.com sat jan 5 09:14:16 2019'
y = re.findall('^From (\S+@\S+)',x) #!!!!! Regular Expressions is case sensitive
print(y) # The '\S+@\S+' The '\S' is mean non-whitespace character
# '\S+@\S+' means at least one non-whitespace character
print("\n")
print("Test case 6 end \n")

# Case 7 is extract the domain name of email addresses
print("Test case 7 start\n")

data = "From leejianzhi@lee.com Sat Jan 5 09:14:16 2019"
find_at = data.find('@') #find '@' in a string
print('@ is at the index postion ',find_at) #return the index position os '@'

whiteSpace = data.find(' ', find_at) #find the white space after the '@'
#the reason for doing that is the domain name I am trying to extract is between '@' amd the first whitespace after @
print('White Space after the "@" is at the index position', whiteSpace)

domain_name = data[find_at+1 : whiteSpace] #string slicing to find the position beyond the @ and up to but not include the first whitespace afater @
print('The email domain name is : ',domain_name)

print("\n")
print("Use Double Split Parttern to extract email domain name: ")
print("\n")

words = data.split()
#print(words)

email = words[1]
#print('Email address is:', email)

email_domain = email.split('@')
#print('Seperate the user and domain domain_name: ', email_domain)
print('The email server domain is : ', email_domain[1])

print("\n")
print("Test case 7 end \n")

print("Test case 8 start\n")
print("Regex method\n")

y = re.findall('@([^ ]*)',data)
print('Method 1: ',y)
# Find the @ sign first, then [^ ] match non-blank char, means everything
#but space -> non blank... match many of them

#Second method

y = re.findall('^From .*@([^ ]*)', data)
print('Method 2: ',y)
#start with beginning of the line, looking for the string 'From' with space
print("\n")
print("Test case 8 end \n")
