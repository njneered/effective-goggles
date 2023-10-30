

#decode function
def decode_password(decode_input):
	decode_input_list = []
	for i in decode_input:
		i = int(i) - 3
		decode_input_list.append(i)
		decoded_string = "".join(map(str, decode_input_list))
	return decoded_string


