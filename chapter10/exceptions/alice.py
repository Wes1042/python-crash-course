

file_name = 'alice.txt'

try:
    with open(file_name, encoding="utf_8") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist"
    print(msg)
else:
    # Count the approzimate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")