class Student:
    university = "Jala"
    
    def __init__(self, name: str, lastname: str, year: int):
        self.__name = name
        self.__lastname = lastname
        self.__year = year

    def presentation(self):
        print("My name is {}".format(self.__name))
        print("My lastname is {}".format(self.__lastname))
        print("I have {} years old".format(self.__year))
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print("Setting... Name")
        self.__name = new_name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, new_lastname):
        print("Setting... Lastname")
        self.__lastname = new_lastname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        print("Setting... Age")
        self.__age = new_age


name = input("[+] Enter your name: ")
print(f"my name is {name}")

lastname = input("[+] Enter your lastname: ")
print(f"my lastname is {lastname}")

age = input("[+] Enter your age: ")
print(f"my age is {age}")
print(type(age))

student_1 = Student(name, lastname, age)
student_1.presentation()