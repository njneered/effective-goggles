# encode
def encoder(message):
	result = ""
	for number in message:
		new_number = str((int(digit) + 3) % 10)
		result += new_number
	return result

# decode

# menu
def main():
	while True:
		print("Menu")
		print("-------------")
		print("1. Encode")
		print("2. Decode")
		print("3. Quit")
		user_input = input("Please enter an option: ")

		if user_input == "1":
			prompt = input("Please enter your password to encode: ")
			print("Your password has been encoded and stored!")
		elif user_input == "2":
			prompt = input("The encoded password is," encoder(prompt), "and the original password is" decoder(prompt))
		elif choice == "3":
			break

