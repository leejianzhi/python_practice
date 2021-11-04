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

if __name__ == "__main__":


	list_operation()
