import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from PIL import Image, ImageTk
import tkinter as tk
from Amain import PBSIR_System

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1530x790+0+0")
        self.master.title("Photo based Student Information Retrieval System - (Admin Login Window)")

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        self.my_cursor = self.conn.cursor()

        # left_label frame
        l_frame = LabelFrame(master, bd=20, bg="white", relief=RIDGE)
        l_frame.place(x=510, y=175, width=500, height=400)

        Label(l_frame, text="Admin Login", bg="#c0ecc0", fg="black", width="300", height="2", font=("Calibri", 13)).pack(
            padx=20, pady=23)
        Label(l_frame, text="",bg="#ffffff").pack()

        Label(l_frame, text="Username", fg="black", bg="#c0ecc0").pack()
        self.entry_username = Entry(l_frame)
        self.entry_username.pack(pady=5)

        Label(l_frame, text="Password", fg="black", bg="#c0ecc0").pack(pady=5)
        self.entry_password = Entry(l_frame, show='*')
        self.entry_password.pack()

        Label(l_frame, text="",bg="#ffffff").pack()
        Button(l_frame, text="Login", width=10, fg="black", height=1, command=self.login).pack()
        Label(l_frame, text="",bg="#ffffff").pack()
        Label(l_frame, text="Not Yet Registered?", fg="black", bg="#ff6bbe").pack(pady=10)
        Button(l_frame, text="Register Now", width=10, fg="black", height=1, command=self.open_admin_Verification_window).pack()


    def open_admin_Verification_window(self):
        register_Verification_window = Toplevel(self.master)
        AdminRegistrationCheck(register_Verification_window)



    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Query to check username and password
        query = "SELECT * FROM admins WHERE username = %s AND password = %s"
        self.my_cursor.execute(query, (username, password))
        result = self.my_cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.open_home_window()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_home_window(self):
        self.new_window = Toplevel(self.master)
        self.app = PBSIR_System(self.new_window)






valid_emp_ids = ["102", "103", "107", "10342", "102221"]  # Add more if needed



class AdminRegistrationCheck:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")
        self.master.title("Admin Registration")

        self.load_valid_emp_ids()

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        self.my_cursor = self.conn.cursor()

        # Frame
        frame = LabelFrame(master, text="Admin Registration", padx=20, pady=20)
        frame.pack(padx=50, pady=50)

        # Labels and Entries
        Label(frame, text="Employee ID:").grid(row=0, column=0, sticky="w")
        self.entry_emp_id = Entry(frame)
        self.entry_emp_id.grid(row=0, column=1)

        # Button
        Button(frame, text="Register", command=self.register_admin_check).grid(row=2, columnspan=2)


    def load_valid_emp_ids(self):
        global valid_emp_ids
        with open("valid_emp_ids.txt", "r") as file:
            valid_emp_ids = file.read().splitlines()


    def register_admin_check(self):

        global emp_id1
        emp_id1 = self.entry_emp_id.get()

        # Query to check employee ID
        query = "SELECT * FROM admins WHERE emp_id = %s"
        self.my_cursor.execute(query, (emp_id1,))
        result = self.my_cursor.fetchone()

        if result:
            messagebox.showerror("Error...", "Employee ID already Registered")
        else:
            if emp_id1 in valid_emp_ids:
                messagebox.showinfo("Employee ID Successful Verified!!", "Welcome, Upcoming Admin!")
                self.open_admin_registration(emp_id1)
            else:
                messagebox.showerror("Error...","Invalid employee ID")

#messagebox.showerror("Employee ID already Registered","Employee ID already Registered" "\n                      or" " \n        Invalid employee ID")


    def open_admin_registration(self, emp_id):
        register_window = Toplevel(self.master)
        AdminRegistration(register_window, emp_id)




class AdminRegistration():
    def __init__(self, master, emp_id):
        self.master = master
        self.master.geometry("1530x790+0+0")
        self.master.title("Admin Registration")

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        self.my_cursor = self.conn.cursor()

        print(emp_id)


        # left_label frame
        l_frame = LabelFrame(master, bd=20, bg="white", relief=RIDGE)
        l_frame.place(x=510, y=175, width=500, height=420)

        Label(l_frame, text="Admin Registration", bg="#c0ecc0", fg="black", width="300", height="2", font=("Calibri", 13)).pack(
            padx=20, pady=23)
        Label(l_frame, text="",bg="#ffffff").pack()

        Label(l_frame, text="Username", fg="black", bg="#c0ecc0").pack()
        self.entry_username = Entry(l_frame)
        self.entry_username.pack(pady=5)

        Label(l_frame, text="Password", fg="black", bg="#c0ecc0").pack()
        self.entry_password = Entry(l_frame)
        self.entry_password.pack(pady=5)

        Label(l_frame, text="Name", fg="black", bg="#c0ecc0").pack()
        self.entry_name = Entry(l_frame)
        self.entry_name.pack(pady=5)

        Label(l_frame, text="Employee ID:", fg="black", bg="#c0ecc0").pack()
        self.entry_emp_id = Entry(l_frame)
        #self.entry_emp_id = Entry(l_frame, state='readonly')
        #self.entry_emp_id.insert(0, emp_id)
        self.entry_emp_id.pack(pady=5)
        


        
        Label(l_frame, text="",bg="#ffffff").pack()
        Button(l_frame, text="Register", width=10, fg="black", height=1, command=self.register_admin).pack()

        

    def register_admin(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        name = self.entry_name.get()
        emp_id = self.entry_emp_id.get()

        # Check if employee ID is unique
        if self.emp_id_check(emp_id):
            messagebox.showerror("Employee ID Error", "Employee ID You entered for verification is differrent!!.")
            return

        # Check if password meets the criteria
        if not self.validate_password(password):
            messagebox.showerror("Password Error", "Password should have 8 characters with a combination of "
                                                   "lowercase, uppercase letters, numbers, and special characters.")
            return
        
        # Check if employee ID is unique
        if not self.is_emp_id_unique(emp_id):
            messagebox.showerror("Employee ID Error", "Employee ID is already registered.")
            return

        # Insert into database
        query = "INSERT INTO admins (username, password, name, emp_id) VALUES (%s, %s, %s, %s)"
        values = (username, password, name, emp_id)
        self.my_cursor.execute(query, values)
        self.conn.commit()

        messagebox.showinfo("Registration Successful", "Admin registered successfully!")
        self.remove_emp_id(emp_id)


    def validate_password(self, password):
        if len(password) != 8:
            return False

        lowercase = any(c.islower() for c in password)
        uppercase = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(not c.isalnum() for c in password)

        return lowercase and uppercase and digit and special
    

    def is_emp_id_unique(self, emp_id):
        query = "SELECT * FROM admins WHERE emp_id = %s"
        self.my_cursor.execute(query, (emp_id,))
        result = self.my_cursor.fetchone()
        return result is None
    
    
    def emp_id_check(self, emp_id):
        emp_id = self.entry_emp_id.get()
        print(emp_id)
        if emp_id != emp_id1:
            return True
        else:
            return False
        

    def load_valid_emp_ids(self):
        global valid_emp_ids
        with open("valid_emp_ids.txt", "r") as file:
            valid_emp_ids = file.read().splitlines()

    
    def remove_emp_id(self, emp_id):
        global valid_emp_ids  # Declare global to modify the global variable
        if emp_id in valid_emp_ids:
            valid_emp_ids.remove(emp_id)
            print(f"Employee ID {emp_id} removed successfully.")
            self.save_valid_emp_ids()  # Save the updated list
        else:
            print(f"Employee ID {emp_id} not found in the valid list.")


    def save_valid_emp_ids(self):
        global valid_emp_ids
        with open("valid_emp_ids.txt", "w") as file:
            file.write("\n".join(valid_emp_ids))


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()