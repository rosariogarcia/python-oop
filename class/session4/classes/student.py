class Student():
    #propiedades de clase
    #es accesible directamente
    #sin necesidad de crear una instancia
    university = "Jala"

    ##constructor con datos por defecto
    #def __init__(self):
    #    self.name = "Rosario"
    #    self.lastname ="Garcia"
    #    self.year = 29

    
    ##constructor con parametros
    def __init__(self, name: str, lastname: str, year: int):
        self.__name = name
        self.__lastname =lastname
        self.__year = year

    def presentation(self):
        print(f"My name is {self.__name}")
        print(f"My lastname is {self.__lastname}")
        print(f"I have {self.__year}")
        #print(f"I am at {self.__university}")

    # def get_name(self):
    #     return self.__name

    @property
    def name(self):
        return self.__name
    

    # def get_name(self):
    #     return self.__name

    @name.setter
    def set_name(self, name):
        print("Setting name")
        self.__name = name
#instancia
#student = Student()

#usos
# print(f"My name is {student.name}")
# print(f"My lastname is {student.lastname}")
# print(f"I have {student.year}")

# #acceder a la propiedad de clase
# print(f"I'm at {student.university} universitty")
# print(f"I'm at {Student.university} universitty")

# #Modificando valores
# student.name = "name"
# print(f"My name is {student.name}")

# student.lastname = "lastname"
# print(f"My lastname is {student.lastname}")


#instancia
# student2 = Student("Andres", "Santos", 23)

#usos
# print(f"My name is {student2.name}")
# # print(f"My lastname is {student2.lastname}")
# # print(f"I have {student2.year}")

# ##las variables de clase cambian para todas las instancias
# Student.university = "UMRPSFX"

# #
# student1 = Student("Gramzi","hermoso",23)
# student1.presentation()

# student2 = Student("Gramsci","hermoso",31)
# student2.presentation()

# student3 = Student("Andres","Santos",31)
# student3.presentation()

# name= input()
name = input("[+] Enter your name: ")
print(f"my name is {name}")

lastname = input("[+] Enter your lastname: ")
print(f"my lastname is {lastname}")

age = input("[+] Enter your age: ")
print(f"my age is {age}")
print(type(age))

student_1 = Student(name, lastname, age)
student_1.presentation()


