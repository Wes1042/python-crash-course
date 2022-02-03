print("Give me 2 numbers and I will add them")
print("To quit the program , enter 'q'")
while True:
    try:
        number1 = input("Number 1 :")
        if number1 == 'q':
            break
        else: 
            number1 = int(number1)

        number2= input("Number 2 : ")
        if number2 == 'q':
            break
        else:
            number2 = int(number2)    
            
    except ValueError:
        print("Please enter a number and not a word\n")
    else: 
        sum = int(number1) + int(number2)
        print( str(sum) + '\n')
