


def read_file(file_name):
    try:
        with open(file_name) as file:
            contents = file.read()
    except FileNotFoundError:
        msg = ("The file '"+ file_name + "' does not exist...")
        print(msg)
        #pass #for silent error
    else:
        print(contents)

file_name = read_file('dogs.txt')
file_name = read_file('cat.txt')