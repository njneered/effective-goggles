# encode
def encoder(message):
    result = ""
    for number in message:
        new_number = str((int(digit) + 3) % 10)
        result += new_number
    return result
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
                prompt = input("The encoded password is,", encoder(prompt), "and the original password is", decode_password(encoder(prompt)),".")
            elif user_input == "3":
                break

#decode function
def decode_password(decode_input):
	decode_input_list = []
	for i in decode_input:
		i = int(i) - 3
		decode_input_list.append(i)
		decoded_string = "".join(map(str, decode_input_list))
	return decoded_string




