
file_name = "poll-book.txt"


while True:
    print("type 'q' to stop the program")
    name = input('Please enter your name:\n')
    if name == 'q':
        break
    else:
        with open(file_name , 'a')as file_object:
            while True:
                print('Hello ' + name )
                poll_input = input('Why do you like programming? : \n')
                file_object.write(name + ' : ' + poll_input + ' \n')
                print("Thank you for your input :)\n")
                break
                
           


        