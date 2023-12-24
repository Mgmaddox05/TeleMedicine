import tkinter as tk
from tkinter import ttk

# Create a dictionary to store user data (in-memory simulation)
user_data = {}

def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    signup_label = tk.Label(signup_window, text="Sign Up for Telehealth", font=("Arial", 16))
    signup_label.pack(pady=10)

    name_label = tk.Label(signup_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(signup_window)
    name_entry.pack()

    email_label = tk.Label(signup_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(signup_window)
    email_entry.pack()

    password_label = tk.Label(signup_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(signup_window, show="*")
    password_entry.pack()

    def perform_signup():
        user_name = name_entry.get()
        user_email = email_entry.get()
        user_password = password_entry.get()

        # Check if the email is already registered
        if user_email in user_data:
            print("Email is already registered.")
        else:
            # Store the user's information in the dictionary (simulated database)
            user_data[user_email] = {
                "name": user_name,
                "password": user_password,
            }
            print("Signed up successfully.")
            signup_window.destroy()

    signup_button = tk.Button(signup_window, text="Sign Up", command=perform_signup)
    signup_button.pack(pady=10)

def open_ehr_page(user_name):
    signin_window.destroy()
    ehr_window = tk.Toplevel(root)
    ehr_window.title("Electronic Health Record")

    ehr_label = tk.Label(ehr_window, text=f"EHR Page - Welcome, {user_name}", font=("Arial", 16))
    ehr_label.pack(pady=10)

    # Create a notebook widget for tabs
    notebook = ttk.Notebook(ehr_window)
    notebook.pack(pady=10)

    # Create a "Patient Info" tab
    patient_info_tab = ttk.Frame(notebook)
    notebook.add(patient_info_tab, text="Patient Info")

    # Sample patient data
    patient_data = {
        "Name": "Matthew Maddox",
        "DOB": "September 29th, 2005",
        "Height": "5'11\"",
        "Weight": "174 lbs",
        "Blood Type": "O+",
        "Allergies": "Sudden Weather Changes",
        "Medical History": "Eplisey",
    }

    # Display patient data using labels in the "Patient Info" tab
    for i, (key, value) in enumerate(patient_data.items()):
        label = tk.Label(patient_info_tab, text=f"{key}: {value}", font=("Times New Roman", 30))
        label.grid(row=i, column=0, sticky="w")

    # Create a "Calendar" tab
    calendar_tab = ttk.Frame(notebook)
    notebook.add(calendar_tab, text="Calendar")

    # Add a calendar widget or any calendar-related components in the "Calendar" tab
    calendar_label = tk.Label(calendar_tab, text="Calendar will go here", font=("Arial", 12))
    calendar_label.pack()

    # Create a "Account Info" tab
    accInfo_tab = ttk.Frame(notebook) 
    notebook.add(accInfo_tab, text="Account Info")

    # Create a ""

    

# Create the main window
root = tk.Tk()
root.title("Telehealth App")

# Add a "Sign Up" button on the main page
signup_button = tk.Button(root, text="Sign Up", command=open_signup_window)
signup_button.pack(pady=10)

def open_signin_window():
    signin_window = tk.Toplevel(root)
    signin_window.title("Sign In")

    signin_label = tk.Label(signin_window, text="Sign In to Telehealth", font=("Arial", 16))
    signin_label.pack(pady=10)

    email_label = tk.Label(signin_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(signin_window)
    email_entry.pack()

    password_label = tk.Label(signin_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(signin_window, show="*")
    password_entry.pack()

    def perform_signin():
        user_email = email_entry.get()
        user_password = password_entry.get()

        # Check if the email exists in the dictionary and the password matches
        if user_email in user_data and user_data[user_email]["password"] == user_password:
            print("Signed in successfully as", user_data[user_email]["name"])
            open_ehr_page(user_data[user_email]["name"])
            signin_window.destroy()
        else:
            print("Invalid credentials. Please try again.")

    signin_button = tk.Button(signin_window, text="Sign In", command=perform_signin)
    signin_button.pack(pady=10)

# Add a "Sign In" button on the main page
signin_button = tk.Button(root, text="Sign In", command=open_signin_window)
signin_button.pack(pady=10)

tk.mainloop()
