'''Read the program like:
Try doing the following code
however when this error/code appears 
Run this other code
'''

"""Another way to see it:
Run some code and if the code comes accorss
a specific error or result
run code based on that error"""

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else: # << else if no unexpected result appears , do the following
        print(answer)
        #break
