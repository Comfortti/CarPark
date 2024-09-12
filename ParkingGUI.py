import tkinter as tk   
from GUICarPark import CarParkSimulator
from tkinter import messagebox

car_park = CarParkSimulator(total_spaces=10, hourly_rate=2, csv_file='parking_record.csv')

class ParkingGUI: 

    def __init__(self): 

        self.root = tk.Tk()

#Dimensions of the GUI 
        self.root.geometry("1125x600")
        self.root.config(bg="skyblue")
#Sort into Frames 
        self.left_frame = tk.Frame(self.root, width=400, height=500, bg="white")
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        self.right_frame = tk.Frame(self.root, width=400, height=500, bg="white")
        self.right_frame.grid(row=0, column=1, padx=10, pady=5)

#Inser My Image
        image = tk.PhotoImage(file="SCaM_Poster.gif")
        original_image = image.subsample(1,1)
        self.label = tk.Label(self.right_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)
        #self.label.pack(padx=15, pady=15)

#Heading of the GUI 
        self.root.title("SCaM Car Park")

        self.label = tk.Label(self.left_frame, text="Welcome to SCaM Car Park", font=('Verdana', 18), bg = "white")
        self.label.pack(padx=15, pady=15)

        self.label = tk.Label(self.left_frame, text="Please Select an Option Below:", font=('Verdana', 14), bg = "white")
        self.label.pack(padx=5, pady=5)

        self.label = tk.Label(self.left_frame, text="Parking is £2 per hour", font=('Verdana', 12), bg = "white")
        self.label.pack(padx=5, pady=5)

        self.button = tk.Button(self.left_frame, text="Enter Car Park", font=('Verdana', 14), bg = "white", command=self.open_entry_window)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.left_frame, text="Exit Car Park", font=('Verdana', 14), bg = "white", command=self.open_exit_window)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.left_frame, text="Query Parking Ticket", font=('Verdana', 14), bg = "white", command=self.open_query_window)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.left_frame, text="View Available Spaces", font=('Verdana', 14), bg = "white", command=self.display_spaces)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.left_frame, text="Quit", font=('Verdana', 14), bg = "white", command=self.on_closing)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def open_entry_window(self):
        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.title("Enter Car Park")
        self.newWindow.geometry("350x100")
        tk.Label(self.newWindow, text="Please Enter your Car Registration Plate:").pack()
        self.entry = tk.Entry(self.newWindow)
        self.entry.pack()
        tk.Button(self.newWindow, text="Submit", command = self.entry_submit).pack()

    def open_exit_window(self):
        self.exitWindow = tk.Toplevel(self.root)
        self.exitWindow.title("Exit Car Park")
        self.exitWindow.geometry("350x100")
        tk.Label(self.exitWindow, text="Please Enter your Ticket Number:").pack()
        self.exit = tk.Entry(self.exitWindow)
        self.exit.pack()
        tk.Button(self.exitWindow, text="Submit", command = self.exit_submit).pack()

    def open_query_window(self):
        self.QWindow = tk.Toplevel(self.root)
        self.QWindow.title("Ticket Query")
        self.QWindow.geometry("350x100")
        tk.Label(self.QWindow, text="Please Enter your Ticket Number:").pack()
        self.query = tk.Entry(self.QWindow)
        self.query.pack()
        tk.Button(self.QWindow, text="Submit", command = self.query_submit).pack()

    def entry_submit(self):
        user_input = self.entry.get()
        welcome = car_park.park_car(user_input)
        messagebox.showinfo(title="Parking Information", message=welcome)
        self.newWindow.destroy()

    def exit_submit(self):
        exit_input = self.exit.get()
        goodbye = car_park.process_payment(exit_input)
        messagebox.showinfo(title="Parking Information", message=goodbye)
        self.exitWindow.destroy()

    def query_submit(self):
        query_input = self.query.get()
        query = car_park.show_ticket(query_input)
        messagebox.showinfo(title="Parking Information", message=query)
        self.QWindow.destroy()

    def display_spaces(self):
        display = car_park.display_available_spaces()
        messagebox.showinfo(title="Available Parking Spaces", message=display)


    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


ParkingGUI()