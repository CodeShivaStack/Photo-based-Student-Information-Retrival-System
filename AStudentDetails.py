from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from ttkthemes import ThemedTk
from tkinter import messagebox
import mysql.connector
import cv2
import re
from tkinter import filedialog
import os


class student_info:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Information System")


        #=======variables=====
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_usn=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_paddress=StringVar()
        self.var_taddress=StringVar()
        self.var_photo=StringVar()

        self.var_serchId=StringVar()






        
        # bg_image
        img=Image.open(r"resources/23.png")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)

        title_lbl=Label(bg_img,text="Student Information System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=50 ,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=110,width=1480,height=660)

        # left_label frame
        l_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        l_frame.place(x=10,y=10,width=720,height=580)

        #image
        img1=Image.open(r"resources/22.png")
        img1=img1.resize((1530,710),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(l_frame,image=self.photoimg1)
        bg_img.place(x=5,y=0,width=705,height=135)

        #current course
        currentCourse_frame=LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Details",font=("times new roman",15,"bold"))
        currentCourse_frame.place(x=5,y=135,width=705,height=115)
        
        #department
        Dept_lbl=Label(currentCourse_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        Dept_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CSE","ESE","EEE","MECH","CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        Course_lbl=Label(currentCourse_frame,text="Year of Admission",font=("times new roman",12,"bold"),bg="white")
        Course_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        Course_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        Course_combo["values"]=("Select Year","2020","2021","2022","2023","2024")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_lbl=Label(currentCourse_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_lbl=Label(currentCourse_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #class student information
        ClassStudent_frame=LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",15,"bold"))
        ClassStudent_frame.place(x=5,y=250,width=705,height=300)
        
        #studentId
        studentId_lbl=Label(ClassStudent_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentId_lbl.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        studentId_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_id,width=18,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentName
        studentName_lbl=Label(ClassStudent_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        studentName_lbl.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        studentName_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_name,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #studentUSN
        studentUSN_lbl=Label(ClassStudent_frame,text="USN",font=("times new roman",12,"bold"),bg="white")
        studentUSN_lbl.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        studentUSN_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_usn,width=18,font=("times new roman",13,"bold"))
        studentUSN_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #studentGender
        studentGender_lbl=Label(ClassStudent_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        studentGender_lbl.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        studentGender_combo=ttk.Combobox(ClassStudent_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        studentGender_combo["values"]=("Select Gender","Male","Female","Other")
        studentGender_combo.current(0)
        studentGender_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #studentGender_entry=ttk.Entry(ClassStudent_frame,width=20,font=("times new roman",13,"bold"))
        #studentGender_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #studentEmail
        studentEmail_lbl=Label(ClassStudent_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        studentEmail_lbl.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        studentEmail_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        studentEmail_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #studentPhone
        studentPhone_lbl=Label(ClassStudent_frame,text="Phone No.",font=("times new roman",12,"bold"),bg="white")
        studentPhone_lbl.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        studentPhone_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        studentPhone_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #studentPAddress
        studentPAddress_lbl=Label(ClassStudent_frame,text="Permanent Address",font=("times new roman",12,"bold"),bg="white")
        studentPAddress_lbl.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        studentPAddress_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_paddress,width=18,font=("times new roman",13,"bold"))
        studentPAddress_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #studentTAddress
        studentTAddress_lbl=Label(ClassStudent_frame,text="Temporary Address",font=("times new roman",12,"bold"),bg="white")
        studentTAddress_lbl.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        studentTAddress_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_taddress,width=18,font=("times new roman",13,"bold"))
        studentTAddress_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #radioButtons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(ClassStudent_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(ClassStudent_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)


        #Buttons_frame
        btn_frame=LabelFrame(ClassStudent_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,command=self.add_data,text="Save",width="17",font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,command=self.update_data,text="Upadte",width="17",font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width="17",font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width="17",font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=LabelFrame(ClassStudent_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=715,height=35)

        takePhoto_btn=Button(btn_frame1,text="Upload Photo",command=self.upload_and_save_picture,width="35",font=("times new roman",13,"bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=0,column=0)

        updatePhoto_btn=Button(btn_frame1,text="Update Photo",command=self.update_and_save_picture,width="35",font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatePhoto_btn.grid(row=0,column=1)






  



        # right_label frame
        r_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Search Details",font=("times new roman",15,"bold"))
        r_frame.place(x=740,y=10,width=720,height=580)


        #image
        img2=Image.open(r"resources/21.png")
        img2=img2.resize((1530,710),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg_img=Label(r_frame,image=self.photoimg2)
        bg_img.place(x=5,y=0,width=705,height=135)

        #Search_system
        search_frame=LabelFrame(r_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        search_frame.place(x=5,y=135,width=705,height=80)

        search_lbl=Label(search_frame,text="Search by:",font=("times new roman",15,"bold"),bg="white")
        search_lbl.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Student_ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=8,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_serchId,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",command=self.fetch_data1,width="13",font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=3,sticky=W)
  
        showall_btn=Button(search_frame,text="Show All",command=self.fetch_data,width="13",font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=3,sticky=W)

        #table_frame
        table_frame=LabelFrame(r_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=225,width=705,height=300  )

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","usn","gender","email","phone","paddress","taddress","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Year of Admission")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("usn",text="USN")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("paddress",text="Permanent Address")
        self.student_table.heading("taddress",text="Temp Address")
        self.student_table.heading("photo",text="Photo sample status")
        #self.student_table.heading("photo",text="")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="105")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("id",width="100")
        self.student_table.column("name",width="100")
        self.student_table.column("usn",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("email",width="150")
        self.student_table.column("phone",width="100")
        self.student_table.column("paddress",width="150")
        self.student_table.column("taddress",width="150")
        self.student_table.column("photo",width="100")
        #self.student_table.column("",width="100")

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()





    def upload_and_save_picture(self):
        # master = tk.Tk()
        # master.withdraw()  # Hide the main window

        student_id = self.var_id.get()
        
        # Open the file explorer
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        
        # Check if a file is selected
        if file_path:
            # Save the selected picture with the student_id
            filename, self.var_photo = self.save_image(student_id, file_path)
            if filename:
                print("Image saved successfully.")
                # print("Photo variable updated to:", self.var_photo)
            else:
                print("Failed to save image.")
        else:
            print("No picture selected.")



    def save_image(self, student_id, image_path):
        try:
            # Check if the image file exists
            if os.path.exists(image_path):
                # Assuming student_id is unique and used as part of the image filename
                filename = f"{student_id}.jpg"
                
                # Path where you want to save the image in your project folder
                save_path = os.path.join("images", filename)
                
                # Copy the image file to the project folder
                with open(image_path, 'rb') as fsrc:
                    with open(save_path, 'wb') as fdst:
                        fdst.write(fsrc.read())
                
                # Update the photo variable
                # self.photo = 1
                self.var_photo.set("1")
                self.update_data()
                
                return filename, self.var_photo
            else:
                print("Image file does not exist.")
                # If the image file doesn't exist, set photo variable to 0
                self.var_photo.set("0")
                self.update_data()
                return None, self.var_photo
            
        except Exception as e:
            print("Error:", e)
            # If an error occurs, set photo variable to 0
            # self.photo = 0
            self.var_photo.set("0")
            return None, self.var_photo
        


    def update_and_save_picture(self):

        student_id = self.var_id.get()

        # Query to check if an image exists for the student
        conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
        query = "SELECT photo FROM student_info WHERE id = %s"
        my_cursor=conn.cursor()
        my_cursor.execute(query, (student_id,))
        result = my_cursor.fetchone()

        if result:
            photo_exists = result[0]  # Assuming the photo column contains either 1 or 0
            if photo_exists:
                # If a photo exists, delete it first
                print("Photo Exists!!")
                self.delete_image(student_id)
            else:
                print("No photo Exists!!")

        # Call the function to upload and save a new picture
        self.upload_and_save_picture()



    # def delete_image(self, student_id):
    #     try:
    #         # Assuming student_id is used as part of the image filename
    #         filename = f"{student_id}.jpg"
            
    #         # Path to the image file
    #         image_path = os.path.join("images", filename)
            
    #         # Check if the image file exists
    #         if os.path.exists(image_path):
    #             # Delete the image file
    #             os.remove(image_path)
    #             print("Image deleted successfully.")
    #         else:
    #             print("Image does not exist.")
    #     except Exception as e:
    #         print("Error:", e)



    def delete_image(self, student_id):
        try:
            # Assuming student_id is used as part of the image filename
            filename_jpg = f"{student_id}.jpg"
            filename_png = f"{student_id}.png"
            
            # Path to the image file (JPG)
            image_path_jpg = os.path.join("images", filename_jpg)
            # Path to the image file (PNG)
            image_path_png = os.path.join("images", filename_png)
            
            # Check if the image file (JPG) exists
            if os.path.exists(image_path_jpg):
                # Delete the image file (JPG)
                os.remove(image_path_jpg)
                print("JPG Image deleted successfully.")
            # Check if the image file (PNG) exists
            elif os.path.exists(image_path_png):
                # Delete the image file (PNG)
                os.remove(image_path_png)
                print("PNG Image deleted successfully.")
            else:
                print("Image does not exist.")
        except Exception as e:
            print("Error:", e)








    #========Function to generate_student_id==========
    
    def generate_student_id(self):
        # Retrieve the last student ID from the database
        conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT MAX(id) FROM student_info")
        last_id = my_cursor.fetchone()[0]

        # If there are no existing users, start from 48700001
        if last_id is None:
            return 48700001

        # Increment the last student ID by 1
        return last_id + 1


    #========Function to add data==========self.var_id=self.generate_student_id()
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            
            #id = self.var_id.get()
            email = self.var_email.get()
            usn = self.var_usn.get()
            phone = self.var_phone.get()

            self.var_idd=self.generate_student_id()

            # Check if USN meets the criteria
            if not self.validate_usn(usn):
                messagebox.showerror("USN Error", "Invalid USN format. It should start with '4HG' followed by year, branch, "
                                                "and student type (regular or lateral) and roll number.")
                return
            
            # Check if email meets the criteria
            if not self.validate_email(email):
                messagebox.showerror("Email Error", "Please enter a valid email address.")
                return

            # Check if phone meets the criteria
            if not self.validate_phone_number(phone):
                messagebox.showerror("Phone No. Error", "Please enter a valid phone number.")
                return            
            

            try:    
                conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_info values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_idd,
                                                                                                                self.var_name.get(),
                                                                                                                self.var_usn.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_paddress.get(),
                                                                                                                self.var_taddress.get(),
                                                                                                                self.var_photo.get()
                                                                                                                
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as errormsg:
                messagebox.showerror("Error",f"Due To :{str(errormsg)}",parent=self.root)    


    #=========Function to fetch data===========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_info")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #=========Function to fetch data===========
    def fetch_data1(self):
        student_id = self.var_serchId.get()
        conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        my_cursor = conn.cursor()

        # Modify the SQL query to filter data for a specific student
        query = "SELECT * FROM student_info WHERE id = %s"
        my_cursor.execute(query, (student_id,))
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in data:
                self.student_table.insert("", END, values=row)
            conn.commit()
        
        conn.close()



    #=========Function to fetch data===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_usn.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_paddress.set(data[10]),
        self.var_taddress.set(data[11]),
        self.var_photo.set(data[12])



    #========Function to update data========== 
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:

            # username = self.entry_username.get()
            email = self.var_email.get()
            usn = self.var_usn.get()
            phone = self.var_phone.get()

            # Check if USN meets the criteria
            if not self.validate_usn(usn):
                messagebox.showerror("USN Error", "Invalid USN format. It should start with '4HG' followed by year, branch, "
                                                "and student type (regular or lateral) and roll number.")
                return
            
            # Check if email meets the criteria
            if not self.validate_email(email):
                messagebox.showerror("Email Error", "Please enter a valid email address.")
                return

            # Check if phone meets the criteria
            if not self.validate_phone_number(phone):
                messagebox.showerror("Phone No. Error", "Please enter a valid phone number.")
                return
            
        
            try:
                Upadte=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadte>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_info set dep=%s,course=%s,year=%s,semester=%s,name=%s,usn=%s,gender=%s,email=%s,phone=%s,p_address=%s,t_address=%s,photo=%s where id=%s",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_usn.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_paddress.get(),
                                                                                                                self.var_taddress.get(),
                                                                                                                self.var_photo.get(),
                                                                                                                self.var_id.get()
                                                                                                                ))
                else:
                    if not Upadte:
                        return
                messagebox.showinfo("Success","Student info Succesfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ES:
                messagebox.showerror("Error",f"Due To:{str(ES)}",parent=self.root)


    def validate_usn(self, usn):
        # USN format: 4HGYYBBKXX
        if len(usn) != 10:
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
    
    def validate_phone_number(self, phone_number):
        pattern = r'^\+?(\d{1,3})?[-. ]?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$'
        
        if re.match(pattern, phone_number):
            return True
        else:
            return False
        
    def validate_email(self, email):
        # Define the regular expression pattern for an email address
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Check if the input matches the pattern
        if re.match(pattern, email):
            return True
        else:
            return False




    #========Function to delete data========== 
    def delete_data(self):
        if self.var_name.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                    my_cursor=conn.cursor()
                    sql="delete from student_info where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student info Succesfully deleted",parent=self.root)
            except Exception as ES:
                messagebox.showerror("Error",f"Due To:{str(ES)}",parent=self.root)


    #========Function to delete data========== 
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_usn.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_paddress.set("")
        self.var_taddress.set("")
        self.var_photo.set("")




    #============ Generate data set =================
    def gen_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_info")
                myresult=my_cursor.fetchall()
                iid=0
                for x in myresult:
                    iid=iid+1
                my_cursor.execute("update student_info set dep=%s,course=%s,year=%s,semester=%s,name=%s,usn=%s,gender=%s,email=%s,phone=%s,p_address=%s,t_address=%s,photo=%s where id=%s",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_usn.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_paddress.get(),
                                                                                                                self.var_taddress.get(),
                                                                                                                self.var_photo.get(),
                                                                                                                self.var_id.get()==iid+1
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #======Load predefined data on face frontals opencv===========
                face_classifer=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifer.detectMultiScale(gray,1.3,5)
                    #scaling factor-1.3
                    #Minimum neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id=img_id+1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        filename_path="imgdata/user."+str(iid)+"."+str(img_id)+".jpg"
                        cv2.imwrite(filename_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face) 

                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")

            except Exception as ES:
                messagebox.showerror("Error",f"Due To:{str(ES)}",parent=self.root)
                    









if __name__=="__main__":
    root=ThemedTk(theme="clam")
    obj=student_info(root)
    root.mainloop() 

    
  