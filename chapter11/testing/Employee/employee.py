class Employee():
    def __init__(self,first,last,salary):
        """An method that stores first name , last name and annual salary. """
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self, ammount= 5000):
        """Gives a raise to employees"""
        self.salary+= ammount

