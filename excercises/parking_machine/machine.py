from datetime import datetime

class Machine(object):
    

    def __init__(self, name, input_time):
        self.name = name
        self.input_time = input_time
        self.ticket = {}

 
    def create_ticket(self):

        actual_time = datetime.now()

        self.ticket.setdefault("vehicle", self.name)
        self.ticket.setdefault("date", actual_time.date())
        self.ticket.setdefault("input", self.input_time.time())
        self.ticket.setdefault("output", actual_time.time())

        time_parked = actual_time - self.input_time
        paid = time_parked.seconds * 10
        self.ticket.setdefault("paid", paid)
        self.__print_ticket()

    def __print_ticket(self):
        print("*****************************")
        print(f"Vehicle: {self.ticket['vehicle']}")
        print(f"Details")
        print(f"{self.ticket['date']}")
        print(f"FROM: {self.ticket['date']} {self.ticket['input']}")
        print(f"TO: {self.ticket['date']} {self.ticket['output']}")
        print(f"Paid: {self.ticket['paid']}")
        print("*****************************")

    
    