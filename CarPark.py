# File converted from ipynp to py, interactive menu is a separate tab
#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import datetime
import csv
import datetime

class CarParkSimulator:
    def __init__(self, total_spaces, hourly_rate, csv_file):
        self.parking_record = self.read_csv_file()
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces
        self.hourly_rate = hourly_rate
        self.parking_tickets = {}
        self.parking_space = {p: None for p in range(1, total_spaces + 1)}
        self.csv_file = csv_file
       

    def find_empty_space(self):
        for space, availability in self.parking_space.items():
            if availability is None:
                return space
        return None
        
    def check_reg_number(self, car_plate):
        return 2 <= len(car_plate) <= 8

    def park_car(self, car_plate):
        if not self.check_reg_number(car_plate):
            return print("Invalid Licence Reg Plate. Licence Number should be 2 - 7 characters long. \n Returning to Main Menu.")
            
        empty_space = self.find_empty_space()
        if empty_space is not None:
            ticket_number = len(self.parking_tickets) + 1
            entry_time = datetime.datetime.now()
            self.parking_tickets[ticket_number] = {'car_plate': car_plate, 'entry_time': entry_time, 'space': empty_space}
            self.parking_space[empty_space] = ticket_number  # Marks the space as occupied by the ticket number
            self.available_spaces -= 1
            return print(f"Vehicle Number Plate: '{car_plate}'. Please park in Bay {empty_space}. Ticket number: {ticket_number}. \nAvailable Parking Spaces: {self.available_spaces}/{self.total_spaces}")
        else:
            return print("Sorry, the car park is full.")

    def generate_ticket(self, ticket_number):
        if not ticket_number: 
            print("Invalid Ticket Number. \nFor assistence, please visit www.SCaMParking.co.uk/Help1")
            return None
        ticket_number = int(ticket_number)

        if ticket_number in self.parking_tickets:
            ticket_info = self.parking_tickets[ticket_number]
            car_plate = ticket_info['car_plate']
            entry_time = ticket_info['entry_time']
            space = ticket_info['space']
            print(f"Ticket Information: \nLicence Plate: '{car_plate}' parked in Bay {space}. \nTicket Number: {ticket_number}. \nEntry Time: {entry_time}")
            return entry_time
        else:
            print(f"Invalid ticket number: {ticket_number}. Please provide a valid ticket number.")
            return None

    def calculate_fee(self, entry_time):
        exit_time = datetime.datetime.now()
        parked_duration = exit_time - entry_time
        hours_parked = parked_duration.total_seconds() / 3600
        fee = round(hours_parked * self.hourly_rate, 2)
        return fee

    def process_payment(self, ticket_number):
        ticket_number = int(ticket_number)         
        entry_time = self.generate_ticket(ticket_number)
        if entry_time:
            fee = self.calculate_fee(entry_time)
            print(f"Please pay £{fee} for parking. Thank you!")

            # Record exit in CSV file
            self.record_exit(ticket_number, entry_time, fee)

            # Reset the parking space and ticket information
            #del self.parking_tickets[ticket_number]
            self.available_spaces += 1
            print(f"Available parking spaces: {self.available_spaces}/{self.total_spaces}")
        else:
            print("Payment cannot be processed.\nPlease try again.")
# not recording in csv file, likely that the ticket_number is being deleted so the code stops at 
# if ticket_number not in self.parking_tickets because the ticket_number no longer exits             
# source on how to read and write into csv files accesssed from: https://docs.python.org/3/library/csv.html 
    def record_exit(self, ticket_number, entry_time, fee):
        if ticket_number not in self.parking_tickets:
            return print("Ticket has been collected")
             
        exit_time = datetime.datetime.now()
        ticket_info = self.parking_tickets[ticket_number]
        car_plate = ticket_info['car_plate'].upper()
        entry_time = ticket_info['entry_time']
        fee = self.calculate_fee(entry_time)
        space = ticket_info['space']

        with open('parking_record.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([ticket_number, entry_time, exit_time, fee, car_plate, space])

        del self.parking_tickets[ticket_number]
            
    def display_available_spaces(self):
        print(f"Available Parking Spaces: {self.available_spaces}/{self.total_spaces}")

    def read_csv_file(self):
        record_of_parking = [] 
        with open('parking_record.csv', 'r') as csvfile: 
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                record_of_parking.append(row)
            csvfile.close();
        return record_of_parking

def main():
    car_park = CarParkSimulator(total_spaces=10, hourly_rate=2, csv_file='parking_record.csv')

    while True:
        print("\nWelcome to SCaM Student Parking! \nParking is £2 per hour. \nPlease chose a service from the option menu below:")
        print("\nMain Menu:")
        print("1. Enter Car Park")
        print("2. Exit Car Park")
        print("3. View Available Parking Spaces")
        print("4. Query Parking Record by Ticket Number")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            car_plate = input("Enter your vehicle registration number: ")
            car_park.park_car(car_plate)
        elif choice == '2':
            ticket_number = (input("Enter your ticket number for payment: "))
            car_park.process_payment(ticket_number)
        elif choice == '3':
            car_park.display_available_spaces()
        elif choice == '4':
            ticket_number = (input("Enter your ticket number for querying: "))
            car_park.generate_ticket(ticket_number)
        elif choice == '5':
            #car_park.record_exit(ticket_number)
            print("Exiting SCaM Student Parking. Thank you for Visiting!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


# In[ ]:




