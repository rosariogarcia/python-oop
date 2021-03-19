class MyList(object):
    def __init__(self, value):
        self.list = value

    def calculate_list_len(self):
        try:
            return sum(1 for char in self.list)
        except TypeError:
            print(f"The input: {self.list}, is not a list")

class MyString(object):
    def __init__(self, value):
        self.string = value
    
    def calculate_string_len(self):
        try:
            return sum(1 for char in self.string)
        except TypeError:
            print(f"The input: {self.string}, is not a string value")

class MyDictionary(object):
    def __init__(self, value):
        self.dictionary = value
    
    def calculate_dictionary_len(self):
        try:
            return sum(1 for char in self.dictionary)
        except TypeError:
            print(f"The input: {self.dictionary}, is not a dictionary")

def get_len(input_obj):
    if type(input_obj) == MyList:
        return input_obj.calculate_list_len()
    if type(input_obj) == MyString:
        return input_obj.calculate_string_len()
    if type(input_obj) == MyDictionary:
        return input_obj.calculate_dictionary_len()

my_list = MyList(0)
my_string = MyString(1)
my_string_1 = MyString("123")
my_dictionary = MyDictionary({1, 2, 3})

print(get_len(my_list))
print(get_len(my_string))
print(get_len(my_string_1))
print(get_len(my_dictionary))