import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    spouse_name = entry_spouse_name.get()
    num_children = combo_num_children.get()
    child1_age = combo_child1_age.get()
    child2_age = combo_child2_age.get()
    child3_age = combo_child3_age.get()
    address = entry_address.get()
    nationality = entry_nationality.get()
    contact_number = entry_contact_number.get()
    parking_required = combo_parking_required.get()
    email = entry_email.get()

    # Display form data in a message box
    messagebox.showinfo("Form Submission", f"First Name: {first_name}\n"
                                            f"Last Name: {last_name}\n"
                                            f"Spouse Name: {spouse_name}\n"
                                            f"Number of Children: {num_children}\n"
                                            f"Child 1 Age: {child1_age}\n"
                                            f"Child 2 Age: {child2_age}\n"
                                            f"Child 3 Age: {child3_age}\n"
                                            f"Address: {address}\n"
                                            f"Nationality: {nationality}\n"
                                            f"Contact Number: {contact_number}\n"
                                            f"Parking Space Required: {parking_required}\n"
                                            f"Email ID: {email}")

    # Clear the form fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_spouse_name.delete(0, tk.END)
    combo_num_children.current(0)
    combo_child1_age.current(0)
    combo_child2_age.current(0)
    combo_child3_age.current(0)
    entry_address.delete(0, tk.END)
    entry_nationality.delete(0, tk.END)
    entry_contact_number.delete(0, tk.END)
    combo_parking_required.current(0)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Event Registration Form")

# First Name
label_first_name = tk.Label(root, text="First Name:")
label_first_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_first_name = tk.Entry(root)
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

# Last Name
label_last_name = tk.Label(root, text="Last Name:")
label_last_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_last_name = tk.Entry(root)
entry_last_name.grid(row=1, column=1, padx=10, pady=5)

# Spouse Name
label_spouse_name = tk.Label(root, text="Spouse Name:")
label_spouse_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_spouse_name = tk.Entry(root)
entry_spouse_name.grid(row=2, column=1, padx=10, pady=5)

# Number of Children
label_num_children = tk.Label(root, text="Number of Children:")
label_num_children.grid(row=3, column=0, padx=10, pady=5, sticky="e")
children_options = ["0", "1", "2", "3"]
combo_num_children = ttk.Combobox(root, values=children_options)
combo_num_children.current(0)
combo_num_children.grid(row=3, column=1, padx=10, pady=5)

# Child 1 Age
label_child1_age = tk.Label(root, text="Child 1 Age:")
label_child1_age.grid(row=4, column=0, padx=10, pady=5, sticky="e")
child1_age_options = ["0", "Infant", "3-10", "10-15", "15-18", "18-30", "30-40"]
combo_child1_age = ttk.Combobox(root, values=child1_age_options)
combo_child1_age.current(0)
combo_child1_age.grid(row=4, column=1, padx=10, pady=5)

# Child 2 Age
label_child2_age = tk.Label(root, text="Child 2 Age:")
label_child2_age.grid(row=5, column=0, padx=10, pady=5, sticky="e")
child2_age_options = ["0", "Infant", "3-10", "10-15", "15-18", "18-30", "30-40"]
combo_child2_age = ttk.Combobox(root, values=child2_age_options)
combo_child2_age.current(0)
combo_child2_age.grid(row=5, column=1, padx=10, pady=5)

# Child 3 Age
label_child3_age = tk.Label(root, text="Child 3 Age:")
label_child3_age.grid(row=6, column=0, padx=10, pady=5, sticky="e")
child3_age_options = ["0", "Infant", "3-10", "10-15", "15-18", "18-30", "30-40"]
combo_child3_age = ttk.Combobox(root, values=child3_age_options)
combo_child3_age.current(0)
combo_child3_age.grid(row=6, column=1, padx=10, pady=5)

# Address
label_address = tk.Label(root, text="Address:")
label_address.grid(row=7, column=0, padx=10, pady=5, sticky="e")
entry_address = tk.Entry(root)
entry_address.grid(row=7, column=1, padx=10, pady=5)

# Nationality
label_nationality = tk.Label(root, text="Nationality:")
label_nationality.grid(row=8, column=0, padx=10, pady=5, sticky="e")
entry_nationality = tk.Entry(root)
entry_nationality.grid(row=8, column=1, padx=10, pady=5)

# Contact Number
label_contact_number = tk.Label(root, text="Contact Number:")
label_contact_number.grid(row=9, column=0, padx=10, pady=5, sticky="e")
entry_contact_number = tk.Entry(root)
entry_contact_number.grid(row=9, column=1, padx=10, pady=5)

# Parking Space Required
label_parking_required = tk.Label(root, text="Parking Space Required:")
label_parking_required.grid(row=10, column=0, padx=10, pady=5, sticky="e")
parking_required_options = ["Yes", "No"]
combo_parking_required = ttk.Combobox(root, values=parking_required_options)
combo_parking_required.current(0)
combo_parking_required.grid(row=10, column=1, padx=10, pady=5)

# Email ID
label_email = tk.Label(root, text="Email ID:")
label_email.grid(row=11, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=11, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
