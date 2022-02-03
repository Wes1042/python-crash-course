
def count_words(file_name):
    try:
        with open(file_name, encoding="utf_8") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + file_name + " does not exist"
        # print(msg)
        pass # << can be used to continue programs 
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) +
         " words.")  

file_name = ['alice.txt','rara.tx']
for filename in file_name:
    count_words(filename)

