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



if __name__ == "__main__":


	list_slicing()
