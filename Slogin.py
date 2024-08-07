import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from SStudentDetails import Sstudent_info
from about import aboutus



class SLoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1530x790+0+0")
        self.master.title("Photo based Student Information Retrieval System - (Student Login Window)")

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        self.my_cursor = self.conn.cursor()

        # left_label frame
        l_frame = LabelFrame(master, bd=20, bg="white", relief=RIDGE)
        l_frame.place(x=510, y=175, width=500, height=400)

        Label(l_frame, text="Student Login", bg="#c0ecc0", fg="black", width="300", height="2", font=("Calibri", 13)).pack(
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
        Button(l_frame, text="Register Now", width=10, fg="black", height=1, command=self.register_window).pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Query to check username and password
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.my_cursor.execute(query, (username, password))
        result = self.my_cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.studentIdRetrive(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    # def open_home_window(self):
    #     self.new_window = Toplevel(self.master)
    #     self.app = SPBSIR_System(self.new_window)

    # def studentIdRetrive(self,username):
    #     register_window = Toplevel(self.master)
    #     StudentIDRetriever(register_window, username)

    def studentIdRetrive(self,username):
        register_window = Toplevel(self.master)
        SPBSIR_System(register_window, username)

    def register_window(self):
        register_window = Toplevel(self.master)
        RegisterWindow(register_window)



# class StudentIDRetriever:
#     def __init__(self, master, username):
#         self.master = master  # Store the master window


#         # Database connection
#         self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
#         self.my_cursor = self.conn.cursor()

#         self.username = username
#         self.student_id = None
#         self.retrieve_student_id(username)

        

#     def retrieve_student_id(self,username):
#         self.username = username
#         query = "SELECT student_id FROM users WHERE username = %s"
#         self.my_cursor.execute(query, (self.username,))
#         result = self.my_cursor.fetchone()
#         if result:
#             self.student_id = result[0]
#             self.open_home_window(self.student_id)


#     def open_home_window(self,student_id):
#         new_window = Toplevel(self.master)
#         SPBSIR_System(new_window,student_id)





class SPBSIR_System:
    def __init__(self,master,username):
        self.master=master
        self.master.geometry("1530x790+0+0")
        self.master.title("Photo based Student Information Retrival System")
        
        # bg_image
        img=Image.open(r"resources/intro.png")
        img=img.resize((1530,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.master,image=self.photoimg)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(self.master,text="Photo-based Student Information Retrival System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=105)


        #student_button
        img1=Image.open(r"resources/21.png")
        img1=img1.resize((1530,710),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(self.master,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=520,height=220)

        b1=Button(self.master,text="Add Your Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b1.place(x=200,y=300,width=520,height=40)


        #AboutUs
        img4=Image.open(r"resources/24.png")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(self.master,command=self.about,image=self.photoimg4,cursor="hand2")
        b4.place(x=800,y=100,width=520,height=220)

        b4=Button(self.master,command=self.about,text="About Us",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b4.place(x=800,y=300,width=520,height=40)



        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        self.my_cursor = self.conn.cursor()

        self.username = username
        self.student_id = None
        # self.retrieve_student_id(username)


    #====Function Buttons====
    def student_details(self):
        self.retrieve_student_id(self.username)


    def retrieve_student_id(self,username):
        self.username = username
        query = "SELECT student_id FROM users WHERE username = %s"
        self.my_cursor.execute(query, (self.username,))
        result = self.my_cursor.fetchone()
        if result:
            self.student_id = result[0]
            self.open_student_details_window(self.student_id)



    # def open_student_details_window(self,student_id):
    #     self.new_window = Toplevel(self.master)
    #     self.app = Sstudent_info(self.new_window,student_id)

    def open_student_details_window(self,student_id):
        new_window = Toplevel(self.master)
        Sstudent_info(new_window,student_id)


    def about(self):
        self.new_window=Toplevel(self.master)
        self.app=aboutus(self.new_window)





class RegisterWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1530x790+0+0")
        self.master.title("Registration")

        # Database connection
        self.conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        self.my_cursor = self.conn.cursor()

        # left_label frame
        l_frame = LabelFrame(master, bd=20, bg="white", relief=RIDGE)
        l_frame.place(x=510, y=175, width=500, height=400)

        Label(l_frame, text="Student Registration", bg="#c0ecc0", fg="black", width="300", height="2", font=("Calibri", 13)).pack(
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

        Label(l_frame, text="USN", fg="black", bg="#c0ecc0").pack()
        self.entry_usn = Entry(l_frame)
        self.entry_usn.pack(pady=5)
        
        Label(l_frame, text="",bg="#ffffff").pack()
        Button(l_frame, text="Register", width=10, fg="black", height=1, command=self.register_user).pack()


    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        name = self.entry_name.get()
        usn = self.entry_usn.get()

        # Check if password meets the criteria
        if not self.validate_password(password):
            messagebox.showerror("Password Error", "Password should have 8 characters with a combination of "
                                                   "lowercase, uppercase letters, numbers, and special characters.")
            return
        
        # Check if USN meets the criteria
        if not self.validate_usn(usn):
            messagebox.showerror("USN Error", "Invalid USN format. It should start with '4HG' followed by year, branch, "
                                            "and student type (regular or lateral) and roll number.")
            return

        # Generate student ID
        student_id = self.generate_student_id()

        # Insert into database
        query = "INSERT INTO users (username, password, name, usn, student_id) VALUES (%s, %s, %s, %s, %s)"
        values = (username, password, name, usn, student_id)
        self.my_cursor.execute(query, values)
        self.conn.commit()

        messagebox.showinfo("Registration Successful", "User registered successfully!")

    def validate_password(self, password):
        if len(password) != 8:
            return False

        lowercase = any(c.islower() for c in password)
        uppercase = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        special = any(not c.isalnum() for c in password)

        return lowercase and uppercase and digit and special
    
    def validate_usn(self, usn):
        # USN format: 4HGYYBBKXX
        if len(usn) != 10:
            print("0")
            return False

        college_code = usn[:3]
        year = usn[3:5]
        branch = usn[5:7]
        student_type = usn[7:8]
        roll_number = usn[8:]

        # Check if college code is correct
        if college_code != "4HG":
            return False

        # Check if year is in the correct format (YY)
        if not year.isdigit() or int(year) < 19:  # Assuming 20 is the minimum acceptable year
            return False

        # Check if branch is in the correct format (BB)
        valid_branches = ["CS", "CV", "EC", "EE", "ME"]  # Add more if needed
        if branch not in valid_branches:
            return False

        # Check if student type is correct (K)
        if student_type not in ["0", "4"]:
            return False

        # Check if roll number is numeric
        if not roll_number.isdigit():
            return False

        return True

    def generate_student_id(self):
        # Retrieve the last student ID from the database
        self.my_cursor.execute("SELECT MAX(student_id) FROM users")
        last_id = self.my_cursor.fetchone()[0]

        # If there are no existing users, start from 48700001
        if last_id is None:
            return 48700001

        # Increment the last student ID by 1
        return last_id + 1







if __name__ == "__main__":
    root = tk.Tk()
    app = SLoginWindow(root)
    root.mainloop()