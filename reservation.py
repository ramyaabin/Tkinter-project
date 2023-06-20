import tkinter as tk
from tkinter import ttk
import csv

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    gender = combo_gender.get()
    age = entry_age.get()
    booking_id = entry_booking_id.get()
    airline_name = entry_airline_name.get()
    flight_number = entry_flight_number.get()
    origin = entry_origin.get()
    destination = entry_destination.get()
    class_type = combo_class_type.get()
    duration = entry_duration.get()
    price = entry_price.get()

# Append the form data to the CSV file
    with open("C:/Users/Web Developer/Desktop/Oracuz/Python/tkinter-myproject/reservation.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, gender, age, booking_id, airline_name, flight_number, origin, destination,
                        class_type, duration, price])


    # Display success message
    message_label.config(text="Reservation submitted successfully!")

    # Clear the form fields
    entry_name.delete(0, tk.END)
    combo_gender.set("")
    entry_age.delete(0, tk.END)
    entry_booking_id.delete(0, tk.END)
    entry_airline_name.delete(0, tk.END)
    entry_flight_number.delete(0, tk.END)
    entry_origin.delete(0, tk.END)
    entry_destination.delete(0, tk.END)
    combo_class_type.set("")
    entry_duration.delete(0, tk.END)
    entry_price.delete(0, tk.END)

# Create the Tkinter window
root = tk.Tk()
root.title("Reservation Form")

# Create form elements and arrange them in grid

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=1, column=0, padx=10, pady=5)
combo_gender = ttk.Combobox(root, values=["Male", "Female"])
combo_gender.grid(row=1, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=2, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)

label_booking_id = tk.Label(root, text="Booking ID:")
label_booking_id.grid(row=3, column=0, padx=10, pady=5)
entry_booking_id = tk.Entry(root)
entry_booking_id.grid(row=3, column=1, padx=10, pady=5)

label_airline_name = tk.Label(root, text="Airline Name:")
label_airline_name.grid(row=4, column=0, padx=10, pady=5)
entry_airline_name = tk.Entry(root)
entry_airline_name.grid(row=4, column=1, padx=10, pady=5)

label_flight_number = tk.Label(root, text="Flight Number:")
label_flight_number.grid(row=5, column=0, padx=10, pady=5)
entry_flight_number = tk.Entry(root)
entry_flight_number.grid(row=5, column=1, padx=10, pady=5)

label_origin = tk.Label(root, text="Origin:")
label_origin.grid(row=6, column=0, padx=10, pady=5)
entry_origin = tk.Entry(root)
entry_origin.grid(row=6, column=1, padx=10, pady=5)

label_destination = tk.Label(root, text="Destination:")
label_destination.grid(row=7, column=0, padx=10, pady=5)
entry_destination = tk.Entry(root)
entry_destination.grid(row=7, column=1, padx=10, pady=5)

label_class_type = tk.Label(root, text="Class:")
label_class_type.grid(row=8, column=0, padx=10, pady=5)
combo_class_type = ttk.Combobox(root, values=["Economy", "Business", "First"])
combo_class_type.grid(row=8, column=1, padx=10, pady=5)

label_duration = tk.Label(root, text="Duration:")
label_duration.grid(row=9, column=0, padx=10, pady=5)
entry_duration = tk.Entry(root)
entry_duration.grid(row=9, column=1, padx=10, pady=5)

label_price = tk.Label(root, text="Price:")
label_price.grid(row=10, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=10, column=1, padx=10, pady=5)

submit_button = ttk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

message_label = tk.Label(root, text="")
message_label.grid(row=12, column=0, columnspan=2)

root.mainloop()
