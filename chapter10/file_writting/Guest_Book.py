
file_name = "guest_book.txt"

print("type 'q' to stop the program")
while True:
    name = input('Please enter your name:\n')
    if name == 'q':
        break
    else:
        with open(file_name , 'a')as file_object:
            file_object.write(name + '\n')
            print('Hello ' + name + ' We have logged you in the guest book.')


        