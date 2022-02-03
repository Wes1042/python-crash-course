from random import randint
class Die():
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):
        x = randint(1,self.sides)
        print(x)
    
class six_sided_die(Die):
    def __init__(self, sides=6):
        self.sides = sides
        super().__init__(sides) 
           

class ten_sided_die(Die):
    def __init__(self, sides=10):
        self.sides = sides
        super().__init__(sides)

        
class twenty_sides_die(Die):
    def __init__(self,sides = 20 ):
        self.sides = sides
        super().__init__(sides)

# def loop():
#     i = Die()
#     for x in range(i):
#         print(x)


dice1 = six_sided_die()
dice1.roll_die()



# print('\n')
# dice2 = ten_sided_die()
# for x in range(10):
#     dice2.roll_die()

# print('\n')
# dice3 = twenty_sides_die()
# for x in range(10):
#     dice3.roll_die()