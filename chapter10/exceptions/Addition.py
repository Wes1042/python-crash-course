

print("Give me 2 numbers and I will add them")

try:
    number1 = input("Number 1 :")
    number1 = int(number1)

    number2= input("Number 2 : ")
    number2 = int(number2)    
        
except ValueError:
    print("Please enter a number and not a word")
else: 
    print(int(number1) + int(number2))
