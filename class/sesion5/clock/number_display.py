class NumberDisplay():
    def __init__(self, value, limit):
        self.__value= value
        self.__limit= limit

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def increment(self):
        self.__value += 1

    def display(self):
        """
        This function should display the
        value with that format: 00:00, 23:45
        """
        if self.__value<10:
            return f"0{self.__value}"
        else:
            return self.__value

    def __str__(self):
        pass