import tkinter as tk
from tkinter import ttk
import re

# Function to validate the Name
def validate_name(name):
    # Name should only contain letters, and spaces
    return re.match(r"^[A-Za-z\s]+$", name)

# Function to validate the Email
def validate_email(email):
    # Email validation using a simple regular expression
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

# Function to validate the Phone Number
def validate_phone(phone):
    # Phone number validation using a simple regular expression
    return re.match(r"^[0-9]{10}$", phone)

# Create the main window
root = tk.Tk()
root.title("User Profile Form")

# Create and pack a frame for the form elements
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Create and pack form labels and entry widgets
ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Email Id:").grid(row=1, column=0, sticky="w")
email_entry = ttk.Entry(frame)
email_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="Phone Number:").grid(row=2, column=0, sticky="w")
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(frame, text="Gender:").grid(row=3, column=0, sticky="w")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(frame, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(frame, text="Year of Birth:").grid(row=4, column=0, sticky="w")
dob_spinbox = ttk.Spinbox(frame, from_=1900, to=2023)
dob_spinbox.grid(row=4, column=1, padx=10, pady=5)

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    # Validate Name, Email, and Phone Number
    if not validate_name(name):
        result_label.config(text="Invalid Name", foreground="red")
    elif not validate_email(email):
        result_label.config(text="Invalid Email", foreground="red")
    elif not validate_phone(phone):
        result_label.config(text="Invalid Phone Number", foreground="red")
    else:
        result_label.config(text="Form submitted successfully", foreground="green")

# Create and pack a Submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create a label for displaying validation results
result_label = ttk.Label(frame, text="", foreground="green")
result_label.grid(row=6, column=0, columnspan=2, pady=5)

# Start the Tkinter main loop
root.mainloop()
