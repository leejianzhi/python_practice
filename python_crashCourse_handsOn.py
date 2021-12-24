def main():
	print("Hello World")


def remove_space():

	og_message = '       "This a message with space. "         '

	edit_message = og_message.rstrip()


	print("OG   message: ",og_message)
	print("\n")
	print("After remove space: ",edit_message)


def chapter_2():

	user_name = input("Please enter your full name: ")

	print("Hello " + user_name.title() + ",would you like to learn some Python today?")

	print(user_name.title() + " said, if you do not make all the effort for living today, you will fell sorry tomorrow")


def list_del_pop_remove():

	del_list = ["one","two","three","four","five"]
	pop_list = ["one","two","three","four","five"]
	remove_list = ["one","two","three","four","five"]

	del del_list[0]
	print("\n")
	print("The list after DELETE operation is:",del_list,"\n")

	pop_ele = pop_list.pop()

	print("The element has been popped is: ",pop_ele,"\n")
	print("The current list after pop is: ",pop_list,"\n")

	what_remove = 'one'
	remove_list.remove(what_remove)
	print('The list after remove operation is', remove_list,"\n")

	print('The element you removed is',what_remove)

def list_operation():

	wish_to_travel = ["harbin","beijing","quzhou","malaixiya","guangzhou"]

	print("I wish to travel in the list of those cities", wish_to_travel)



	print("Sorted List",sorted(wish_to_travel))

	print("The original list is",wish_to_travel)

	#reverse_list = wish_to_travel.sort(reverse=True)

	print("Reverse sorted list is : ", sorted(wish_to_travel,reverse=True))


def for_loop():

	new_list = ["one","two","three","four","five"]

	for i in new_list:
		print(i)

def chapter_4():

	#use a for loop to print out 1 - 20

	for num in range(1,21):

		print(num)

	#create a list with numer 1 to 1,000,000

	million_list = list(range(1,1000001))

	print(min(million_list),max(million_list),sum(million_list))


	#sum the number 1 - 1000000

	sum_nums = sum(range(1,1000001))

	print("The sum of 1 to 1,000,000 is : ",sum_nums)

	#print odd numbers from 1 - 20

	prime_num = range(1,21,2)

	for i in prime_num:
		if i%2 == 1:
			print("The odd number from 1 - 20 are: ",i)


	# numbers in 3 - 30 can be divided by 3

	divided_3 = range(3,31,3)

	for i in divided_3:
		if i%3 == 0:
			print("Numbers can divided by 3 from 3 to 30 is: ",i)


	#cube numbers

	cube_num_list = range(1,11)

	for i in cube_num_list:

		i = i**3

		print("The result of cube from number 1 to 10 is: ",i) 


	#list comprehension

	cube_com = [i**3 for i in range(1,11)]

	



	print("List comprehension test for cube numbers: ",cube_com)



def list_slicing():

	ex_list = ['1','2','3','4','5']

	print("The original list is： ",ex_list)
	print("The first element in the list is: ",ex_list[:1])
	print("The second element in the list is: ",ex_list[1:2])
	print("The third element in the list is: ",ex_list[2:3])
	print("The fourth element in the list is: ",ex_list[3:4])
	print(("The fifth element in the list is: ",ex_list[4:5]))
	print("By using the '-'' sign to print all : ",ex_list[-5:])


	#chapter 4.4 hands on practice -- slicing
	print("\n")
	print("----------------Chapter 4.4 Hands On---------------- \n",)
	print("The first three items in the list are: ", ex_list[:3])
	# Why we slice the list from the beginning to the 3?
	#Becuase the index is start with 0.

	print("Three items from the middle of the list",ex_list[1:4])

	print("The last three items in the list are: ", ex_list[2:])


	print("\n")
	print("----------------Your Pizza and My Pizza---------------- \n",)


	my_pizza = ["cheese","chicken","beef"]

	friend_pizza = my_pizza[:]
	friend_pizza.append('Fruit')

	print("These are my favourite pizza: ",my_pizza)
	print("These are my friend's pizza: ",friend_pizza)

	for mypizza in my_pizza:
		print("My favourite pizza are: ",mypizza)


	for friendpizza in friend_pizza:
		print("My friends's favourite pizza are: ",friendpizza)
	 




def chap_5():
	print("-------------------------------------")
	print("practice for Tuples")

	new_tuples = ('beef','pork','shrimp','chicken','fruit')

	for print_tuples in new_tuples:
		print("We provide :",print_tuples)

	#test for if the tuples can be modified
	#new_tuples[0] = 'new'

	#other way around to modify tuples
	new_tuples = ('new_001','new_002','shrimp','chicken','fruit')

	for print_tuples in new_tuples:
		print("We provide new menu:",print_tuples)


def chap5_if():

	#alien practice

	#user_input = input("What color of Alien you want to kill? ")

	#alien_color = ['green','yellow','red']

	#if user_input == 'green':
	#	print("You killed a green alien and got 5 points")

	#elif user_input == 'red':
	#	print("You killed a yellow alien and got 10 points")

	#else:
	#	print("You killed a red alien and got 15 points")

	#different ages in human life

	#user_input = int(input("Please input a number of age to determine the stage of life: "))
	"""

	if user_input < 2:
		print("This is a newborn.")

	elif user_input in range(2,4):
		print("This is an infant")
	elif user_input in range(4,13):
		print("This is a todd")
	elif user_input in range(13,20):
		print("This is a teenager")
	elif user_input in range(20,65):
		print("This is an adult.")
	else:
		print("This is a senior.")

	"""
	user_list = ['admin','tom','jerry','mike','rose']
	username_input = input("Please enter your username: ")
	if user_list:
		for userList in user_list:
			if username_input == 'admin':
				print("Hello admin, would you like to see a status report?")
				break
			elif username_input == 'tom':
				print("Hello tom, thank you for logging in again.")
				break
			elif username_input == "mike":
				print("Hello Mike, thank you for logging in again.")
				break
			elif username_input == "rose":
				print("Hello Rose, thank you for logging in again.")
				break
			else:
				print("Sorry, your username have not registered in our system.")
				break

	else:
		print("There is no users.")
	print("\n")
	print("-----------------------------------------------------")
	print("Compare the new username and current username list.")
	print("-----------------------------------------------------")

	current_userlist = ["user1","user2","user3","user4","user5"]
	print("The current userlist is: ",current_userlist)

	new_userlist = ['user1','user2','newuser001','newuser002','newuser003']
	print("The new userlist is: ",new_userlist)

	used_username = []
	canuse_username = []

	for newusers in new_userlist:
		if newusers in current_userlist:
			used_username.append(newusers)
		elif not newusers in current_userlist:
			canuse_username.append(newusers)


	print("The username: ",used_username,"is already in our system")
	print("You can still use: ",canuse_username," to register in our system.")



def dict_prac():

	new_dict = {

			'first_name':'Jason',
			'last_name':'Wang',
			'age':'18',
			'city':'NY'


			}

	for k,v in new_dict.items():
		print(k+':',v)

	print(new_dict['first_name'])


	favourite_language = {

						'Andy':'Python',
						'Jerry':'C',
						'Bob':'C++',
						'Mary':'Java',
						'Bin':'HTML',

						}

	new_list = ['joe','Andy','Jerry','Bob','Mary','Bin','Lily','Jason']

	for name_list in new_list:
		if name_list in favourite_language.keys():
			print(name_list,", thanks for join the program")
		elif name_list not in favourite_language.keys():
			print(name_list,", please join us.")


def chap_6_dict():

	#chap 6.7
	people = {

			'jason':{

					'first_name' : 'jason',
					'last_name' : 'Li',
					'location' : 'NY',

			},

			'mike':{

					'first_name' : 'mike',
					'last_name' : 'Li',
					'location' : 'CA',

			},


			'july':{

					'first_name' : 'kuly',
					'last_name' : 'Li',
					'location' : 'PA',

			},



	}


	for fullname,detail in people.items():
		print("Username: ",fullname,"\n")

		full_name = detail['first_name'] + " " + detail['last_name']
		location = detail['location']


		print("\tFull name: " + full_name.title())
		print("\tLocation: " + location)


	#chap 6.8 pets

	kitty = {

		'pets':['cat','tom']
	}


	for petsinfo in kitty['pets']:
		print("The pets type is: ",petsinfo)
	
		print("The owner's name is: ",petsinfo)


def while_loop():

	magic = True

	message = "\nPlease tell us what you want for your toppings: "
	message += "\nInput 'quit' if you are finished."

	while magic:

		user_input = input(message)

		if user_input == 'quit':
			magic = False

		else:
			print("\nYou added topping: ",user_input)

def show_ticket():

	ask_age = True

	message = "\n Please enter your age to determine a price for you:"

	while ask_age:
		user_input = int(input(message))

		if user_input < 3:
			print("Your ticket is free.")
		elif user_input in range(3,13):
			print("Your ticket is $10.")
		elif user_input > 12:
			print("Your ticket is $15.")

def make_sandwich():

	tag = True

	sandwich_orders = ['tuna','beef','ham','pastrami','pastrami','pastrami','pastrami']

	finished_sandwich = []

	print("The Pastrami sandwich is sold out.")
	while 'pastrami' in sandwich_orders:

		sandwich_orders.remove('pastrami')
		#print("The list after remove is :",sandwich_orders)

		if 'pastrami' not in sandwich_orders:

			for sandwich in sandwich_orders:
				print("I made you a ",sandwich, " sandwich")
				finished_sandwich.append(sandwich)

			print("Today, I made ",finished_sandwich, "sandwiches for customers.")
		
	


def make_shirt(size,print_sentence = 'default print'):


	print('You seleted a T-shirt with size: ',size)
	print('There will be a sentence printed on your T-shirt is: ',print_sentence)



def magician_prac(names):

	for name in names:
		print('Welcome magician name is :',name)

		



def make_greate(greate):

	new_list = []

	for i in greate:
		new_list.append(i + 'the greate')

	for j in new_list:
		print(j)


#page 132 Sandwich prac

def sandwich(*content):

	

	print("You ordered a sandwich with those contents: ")
	for i in content:
		print('-',i)

#user profile prac

def build_profile(first,last,**user_info):

	profile = {}

	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value

	return profile


#8-14 car info


def car_info(brand, model, **package):

 	carinfo = {}

 	carinfo['brand_name'] = brand,
 	carinfo['model'] = model

 	for key,value in package.items():
 		carinfo[key] = value

 	return carinfo

 #chap9 Class prac

 #Example code from the book

class Dog():

 	def __int__(self, name, age):

 		self.name = name
 		self.age = age

 	def sit(self):

 		print(self.name.title() + " is now sitting.")

 	def roll_over(self):

 		print(self.name.title() + " rolled over!")


 	

if __name__ == "__main__":

	my_dog = Dog()

	my_dog.name = 'boa'

	my_dog.age = 6

	print("Test for class, ","My dog's name is: ",my_dog.name, "My dog's age is: ",my_dog.age)
	print(my_dog.sit())

	
	#user_info = build_profile('david','li',location = 'CA',field = 'CS')

	#print(user_info)

	#car = car_info('sabaru','outback',color='blue',tow_package='True')

	#print(car)   