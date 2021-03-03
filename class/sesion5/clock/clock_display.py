from number_display import NumberDisplay

class ClockDisplay:
    def __init__(self, hour, minute):
        self.__hours = NumberDisplay(hour, 24)
        self.__minute = NumberDisplay(minute,59)

    def tick_time(self):
        pass

    def get_time(self):
        pass

    def display(self):
        print("{}:{}".format(self.__hours.display(), self.__minute.display()))


#hour = NumberDisplay(15,24)
#minute = NumberDisplay(15,24)
#clock= ClockDisplay(hour,minute)
#clock.display()

clock= ClockDisplay(15,30)
clock.display()

clock= ClockDisplay(5,5)
clock.display()