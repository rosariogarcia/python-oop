from datetime import datetime
from machine import Machine
import time


class Parking:
    def __init__(self, parking_name="My Parking", capacity=10):
        self.name = parking_name
        self.capacity = capacity
        self.ticket_list = []

    def vehicle_input(self, vehicle_name):
        try:
            if self.capacity > len(self.ticket_list):
                machine = Machine(vehicle_name, datetime.now())
                self.ticket_list.append(machine)
        except:
            print(f"{self.name} is full")

    def vehicle_output(self, vehicle_name):
        if self.ticket_list:
            try:
                for ticket in self.ticket_list:
                    if ticket.name == vehicle_name:
                        ticket.create_ticket()
                        self.ticket_list.remove(ticket)
                        break
            except:
                print(f"{vehicle_name} is not in the parking.") 
        

        
        else:
           print(f"{self.name} is empty") 



parking = Parking()
parking.vehicle_input("auto1")
parking.vehicle_input("auto2")
parking.vehicle_input("auto3")
time.sleep(2)
parking.vehicle_output("auto2")
time.sleep(1)
parking.vehicle_output("auto3")
time.sleep(3)
parking.vehicle_output("auto1")