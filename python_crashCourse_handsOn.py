def main():
	print("Hello World")


def remove_space():

	og_message = '       "This a message with space. "         '

	edit_message = og_message.rstrip()


	print("OG message: ",og_message)
	print("\n")
	print("After remove space: ",edit_message)

if __name__ == "__main__":

	remove_space()