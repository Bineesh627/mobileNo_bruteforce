def number_generate():
    numbers = []
    # You can modify this range according to your usage and purpose.
    for i in range(1000, 10000):
        numbers.append(str(i))
    return numbers

def file_generate():
    numbers = number_generate()
    file_path = "wordlists/contacts.txt"

    with open(file_path, "w") as file:
        for number in numbers:
            # You can modify this to specify which phone number you are searching for.
            text = f"+919281{number}34\n"
            file.write(text)

if __name__ == '__main__':
	print("Creating the list of numbers..")
	file_generate()
	print("Numbers are created...")
