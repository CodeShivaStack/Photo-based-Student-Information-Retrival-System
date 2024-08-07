from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from ttkthemes import ThemedTk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import filedialog
import os
import re

class student_info:
    def __init__(self,master,student_id):
        self.master=master
        self.master.geometry("1530x790+0+0")
        self.master.title("Student Information System")


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


        self.var_deg=StringVar()
        self.var_graduYear=StringVar()
        self.var_cgpa=StringVar()
        self.var_awards=StringVar()
        self.var_projTitle=StringVar()   
        self.var_projDesc=StringVar()
        self.var_projGrade=StringVar()
        self.var_internCom=StringVar()
        self.var_internDur=StringVar()
        self.var_internRole=StringVar()
        self.var_extraCurri=StringVar()

        
        self.var_id.set(student_id)



        
        # bg_image
        img=Image.open(r"resources/23.png")
        img=img.resize((1530,810),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.master,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=810)

        title_lbl=Label(bg_img,text="Student Information System",font=("Georgia",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=50 ,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=110,width=1480,height=660)

        # left_label frame
        l_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Georgia",15,"bold"))
        l_frame.place(x=10,y=10,width=1450,height=580)


        mycanvas=Canvas(l_frame)
        mycanvas.pack(side=LEFT,fill="both",expand="yes")

        scroll_y=ttk.Scrollbar(l_frame,orient=VERTICAL,command=mycanvas.yview)
        scroll_y.pack(side=RIGHT,fill="y")

        mycanvas.configure(yscrollcommand=scroll_y.set)
        mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))


        myframe=LabelFrame(mycanvas)
        mycanvas.create_window((0,0),window=myframe, anchor='nw')
        l_frame.pack(fill="both",expand="yes",padx=10,pady=10)
        

        # for i in range (5):
        #     img11=Image.open(r"resources/24.png")
        #     img11=img11.resize((1530,810),Image.LANCZOS)
        #     self.photoimg=ImageTk.PhotoImage(img11)
        #     bg_img1=Label(myframe,image=self.photoimg).pack()
        #         # #bg_img1.place(x=0,y=0,width=1530,height=810)

        for i in range (2):
            img1=Image.open(r"resources/25.png")
            img1=img1.resize((1530,710),Image.LANCZOS)
            self.photoimg1=ImageTk.PhotoImage(img1)

            bg_img=Label(myframe,image=self.photoimg1).pack()



        #.........................................................................................................................................................................................................................................my button.........................................................................................................................................................................................................................................."+str(i)).pack()
            


        img_frame=LabelFrame(myframe,bd=2,bg="white",relief=RIDGE,font=("Georgia",15,"bold"),background="#c1ff72")
        img_frame.place(x=10,y=35,width=1415,height=135)


    #current course
        currentCourse_frame=LabelFrame(myframe,bd=2,bg="white",relief=RIDGE,text=" Current Course Details ",font=("Georgia",15,"bold"))
        currentCourse_frame.place(x=10,y=205,width=1415,height=115)
        
        #department
        Dept_lbl=Label(currentCourse_frame,text="Department",font=("Georgia",12,"bold"),bg="white")
        Dept_lbl.grid(row=0,column=0,padx=20,sticky=W)
        
        dep_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_dep,font=("Georgia",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CIV","CSE","EEE","ESE","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=30,sticky=W)

        #Course
        Course_lbl=Label(currentCourse_frame,text="Year of Admission",font=("Georgia",12,"bold"),bg="white")
        Course_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        YearOAdm_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_course,font=("Georgia",12,"bold"),state="readonly",width=20)
        YearOAdm_combo["values"]=("Select Year","2020","2021","2022","2023","2024")
        YearOAdm_combo.current(0)
        YearOAdm_combo.grid(row=0,column=3,padx=2,pady=30,sticky=W)

        #year
        year_lbl=Label(currentCourse_frame,text="Year",font=("Georgia",12,"bold"),bg="white")
        year_lbl.grid(row=0,column=4,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_year,font=("Georgia",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020","2021","2022","2023","2024")
        year_combo.current(0)
        year_combo.grid(row=0,column=5,padx=2,pady=30,sticky=W)

        #semester
        semester_lbl=Label(currentCourse_frame,text="Semester",font=("Georgia",12,"bold"),bg="white")
        semester_lbl.grid(row=0,column=6,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_sem,font=("Georgia",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=7,padx=2,pady=30,sticky=W)
        
        
        
    #class student information
        ClassStudent_frame=LabelFrame(myframe,bd=2,bg="white",relief=RIDGE,text=" Class Student Information ",font=("Georgia",15,"bold"))
        ClassStudent_frame.place(x=10,y=350,width=1415,height=240)
        
        #studentId
        studentId_lbl=Label(ClassStudent_frame,text="Student ID",font=("Georgia",12,"bold"),bg="white")
        studentId_lbl.grid(row=0,column=0,padx=35,pady=10,sticky=W)

        studentId_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_id,width=35,font=("Georgia",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentName
        studentName_lbl=Label(ClassStudent_frame,text="Name",font=("Georgia",12,"bold"),bg="white")
        studentName_lbl.grid(row=0,column=2,padx=35,pady=10,sticky=W)

        studentName_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_name,width=35,font=("Georgia",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #studentUSN
        studentUSN_lbl=Label(ClassStudent_frame,text="USN",font=("Georgia",12,"bold"),bg="white")
        studentUSN_lbl.grid(row=1,column=0,padx=35,pady=10,sticky=W)

        studentUSN_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_usn,width=35,font=("Georgia",13,"bold"))
        studentUSN_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #studentGender
        studentGender_lbl=Label(ClassStudent_frame,text="Gender",font=("Georgia",12,"bold"),bg="white")
        studentGender_lbl.grid(row=1,column=2,padx=35,pady=10,sticky=W)

        studentGender_combo=ttk.Combobox(ClassStudent_frame,textvariable=self.var_gender,font=("Georgia",12,"bold"),state="readonly",width=41)
        studentGender_combo["values"]=("Select Gender","Male","Female","Other")
        studentGender_combo.current(0)
        studentGender_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #studentGender_entry=ttk.Entry(ClassStudent_frame,width=35,font=("Georgia",13,"bold"))
        #studentGender_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #studentEmail
        studentEmail_lbl=Label(ClassStudent_frame,text="Email",font=("Georgia",12,"bold"),bg="white")
        studentEmail_lbl.grid(row=2,column=0,padx=35,pady=10,sticky=W)

        studentEmail_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_email,width=35,font=("Georgia",13,"bold"))
        studentEmail_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #studentPhone
        studentPhone_lbl=Label(ClassStudent_frame,text="Phone No.",font=("Georgia",12,"bold"),bg="white")
        studentPhone_lbl.grid(row=2,column=2,padx=35,pady=10,sticky=W)

        studentPhone_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_phone,width=35,font=("Georgia",13,"bold"))
        studentPhone_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #studentPAddress
        studentPAddress_lbl=Label(ClassStudent_frame,text="Permanent Address",font=("Georgia",12,"bold"),bg="white")
        studentPAddress_lbl.grid(row=3,column=0,padx=35,pady=10,sticky=W)

        studentPAddress_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_paddress,width=35,font=("Georgia",13,"bold"))
        studentPAddress_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #studentTAddress
        studentTAddress_lbl=Label(ClassStudent_frame,text="Temporary Address",font=("Georgia",12,"bold"),bg="white")
        studentTAddress_lbl.grid(row=3,column=2,padx=35,pady=10,sticky=W)

        studentTAddress_entry=ttk.Entry(ClassStudent_frame,textvariable=self.var_taddress,width=35,font=("Georgia",13,"bold"))
        studentTAddress_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        # #radioButtons
        # self.var_radio1=StringVar()
        # radiobtn1=ttk.Radiobutton(ClassStudent_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        # radiobtn1.grid(row=5,column=0)
        
        # radiobtn2=ttk.Radiobutton(ClassStudent_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        # radiobtn2.grid(row=5,column=1)






    #class student Academic information
        AcademicInfo_frame=LabelFrame(myframe,bd=2,bg="white",relief=RIDGE,text="Student's Academic Information",font=("Georgia",15,"bold"))
        AcademicInfo_frame.place(x=10,y=625,width=1415,height=410)
        
        #studentId
        studentId_lbl=Label(AcademicInfo_frame,text="Student ID",font=("Georgia",12,"bold"),bg="white")
        studentId_lbl.grid(row=0,column=0,padx=35,pady=10,sticky=W)

        studentId_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_id,width=35,font=("Georgia",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentDegree
        Degree_lbl=Label(AcademicInfo_frame,text="Degree",font=("Georgia",12,"bold"),bg="white")
        Degree_lbl.grid(row=0,column=2,padx=30,pady=10,sticky=W)

        Degree_combo=ttk.Combobox(AcademicInfo_frame,textvariable=self.var_deg,font=("Georgia",12,"bold"),state="readonly",width=41)
        Degree_combo["values"]=("Select Degree","CIV","CSE","EEE","ESE","MECH")
        Degree_combo.current(0)
        Degree_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        

        #studentgraduationYear
        graduationYear_lbl=Label(AcademicInfo_frame,text="Graduation Year",font=("Georgia",12,"bold"),bg="white")
        graduationYear_lbl.grid(row=1,column=0,padx=35,pady=10,sticky=W)

        graduationYear_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_graduYear,width=35,font=("Georgia",13,"bold"))
        graduationYear_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        
        #studentCGPA
        CGPA_lbl=Label(AcademicInfo_frame,text="CGPA",font=("Georgia",12,"bold"),bg="white")
        CGPA_lbl.grid(row=1,column=2,padx=30,pady=10,sticky=W)

        CGPA_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_cgpa,width=35,font=("Georgia",13,"bold"))
        CGPA_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #studentGender_entry=ttk.Entry(AcademicInfo_frame,width=35,font=("Georgia",13,"bold"))
        #studentGender_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #studentAwards
        awards_lbl=Label(AcademicInfo_frame,text="Awards",font=("Georgia",12,"bold"),bg="white")
        awards_lbl.grid(row=2,column=0,padx=35,pady=10,sticky=W)

        awards_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_awards,width=35,font=("Georgia",13,"bold"))
        awards_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #studentProjectTitle
        Projecttitle_lbl=Label(AcademicInfo_frame,text="Project Title.",font=("Georgia",12,"bold"),bg="white")
        Projecttitle_lbl.grid(row=2,column=2,padx=30,pady=10,sticky=W)

        Projecttitle_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_projTitle,width=35,font=("Georgia",13,"bold"))
        Projecttitle_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #studentProjectDesc
        ProjectDescp_lbl=Label(AcademicInfo_frame,text="Project Description",font=("Georgia",12,"bold"),bg="white")
        ProjectDescp_lbl.grid(row=3,column=0,padx=35,pady=10,sticky=W)

        ProjectDescp_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_projDesc,width=35,font=("Georgia",13,"bold"))
        ProjectDescp_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        #studentProjectgrade
        Projectgrade_lbl=Label(AcademicInfo_frame,text="Project Grade",font=("Georgia",12,"bold"),bg="white")
        Projectgrade_lbl.grid(row=3,column=2,padx=30,pady=10,sticky=W)

        Projectgrade_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_projGrade,width=35,font=("Georgia",13,"bold"))
        Projectgrade_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

        #......

        #studentinternshipCom
        internshipCom_lbl=Label(AcademicInfo_frame,text="Internship Company",font=("Georgia",12,"bold"),bg="white")
        internshipCom_lbl.grid(row=4,column=0,padx=35,pady=10,sticky=W)

        internshipCom_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_internCom,width=35,font=("Georgia",13,"bold"))
        internshipCom_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)

        #studentinternshipDur
        internshipDur_lbl=Label(AcademicInfo_frame,text="Internship Duration",font=("Georgia",12,"bold"),bg="white")
        internshipDur_lbl.grid(row=4,column=2,padx=30,pady=10,sticky=W)

        internshipDur_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_internDur,width=35,font=("Georgia",13,"bold"))
        internshipDur_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)

        #studentinternshipRole
        internshipRole_lbl=Label(AcademicInfo_frame,text="Internship Role",font=("Georgia",12,"bold"),bg="white")
        internshipRole_lbl.grid(row=5,column=0,padx=35,pady=10,sticky=W)

        internshipRole_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_internRole,width=35,font=("Georgia",13,"bold"))
        internshipRole_entry.grid(row=5,column=1,padx=10,pady=10,sticky=W)

        #extracurriculars
        extracurriculars_lbl=Label(AcademicInfo_frame,text="Extracurriculars",font=("Georgia",12,"bold"),bg="white")
        extracurriculars_lbl.grid(row=5,column=2,padx=30,pady=10,sticky=W)
        
        extracurriculars_entry=ttk.Entry(AcademicInfo_frame,textvariable=self.var_extraCurri,width=35,font=("Georgia",13,"bold"))
        extracurriculars_entry.grid(row=5,column=3,padx=10,pady=10,sticky=W)


        #Buttons_frame
        btn_frame=LabelFrame(AcademicInfo_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=35,y=290,width=1330,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width="36",font=("Georgia",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Upadte",command=self.update_data,width="36",font=("Georgia",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width="36",font=("Georgia",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        # reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width="27",font=("Georgia",13,"bold"),bg="blue",fg="white")
        # reset_btn.grid(row=0,column=3)

        btn_frame1=LabelFrame(AcademicInfo_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame1.place(x=35,y=325,width=1330,height=35)

        takePhoto_btn=Button(btn_frame1,text="Upload Photo",command=self.upload_and_save_picture,width="55",font=("Georgia",13,"bold"),bg="blue",fg="white")
        takePhoto_btn.grid(row=0,column=0)

        updatePhoto_btn=Button(btn_frame1,text="Update Photo",command=self.update_and_save_picture,width="55",font=("Georgia",13,"bold"),bg="blue",fg="white")
        updatePhoto_btn.grid(row=0,column=1)





    #table_frame
        table_frame=LabelFrame(myframe,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=1085,width=1415,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","usn","gender","email","phone","paddress","taddress","photo","deg","graduYear","cgpa","awards","projTitle","projDesc","projGrade","internCom","internDur","internRole","extraCurri"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
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
        self.student_table.heading("photo",text="Photosamplestatus")

        self.student_table.heading("deg",text="Degree")
        self.student_table.heading("graduYear",text="Graduation Year")
        self.student_table.heading("cgpa",text="CGPA")
        self.student_table.heading("awards",text="Awards")
        self.student_table.heading("projTitle",text="Project Title")
        self.student_table.heading("projDesc",text="Project Description")
        self.student_table.heading("projGrade",text="Project Grade")
        self.student_table.heading("internCom",text="Internship Company")
        self.student_table.heading("internDur",text="Internship Duration")
        self.student_table.heading("internRole",text="Internship Role")
        self.student_table.heading("extraCurri",text="Extracurriculars")
        #self.student_table.heading("photo",text="")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="100")
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

        self.student_table.column("deg",width="100")
        self.student_table.column("graduYear",width="100")
        self.student_table.column("cgpa",width="100")
        self.student_table.column("awards",width="100")
        self.student_table.column("projTitle",width="100")
        self.student_table.column("projDesc",width="100")
        self.student_table.column("projGrade",width="100")
        self.student_table.column("internCom",width="100")
        self.student_table.column("internDur",width="150")
        self.student_table.column("internRole",width="100")
        self.student_table.column("extraCurri",width="150")
        #self.student_table.column("",width="100")

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    # ========Function to upload Image==========

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
        conn=mysql.connector.connect(host="localhost",user="master",passwd="aDmin@321",database="student_data")
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





    



    #========Function to add data==========
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.master)
        else:

            #id = self.var_id.get()
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
                conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_usn.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_paddress.get(),
                                                                                                                self.var_taddress.get(),
                                                                                                                self.var_photo.get(),

                                                                                                                self.var_deg.get(),
                                                                                                                self.var_graduYear.get(),
                                                                                                                self.var_cgpa.get(),
                                                                                                                self.var_awards.get(),
                                                                                                                self.var_projTitle.get(),
                                                                                                                self.var_projDesc.get(),
                                                                                                                self.var_projGrade.get(),
                                                                                                                self.var_internCom.get(),
                                                                                                                self.var_internDur.get(),
                                                                                                                self.var_internRole.get(),
                                                                                                                self.var_extraCurri.get() 
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.master)
            except Exception as errormsg:
                messagebox.showerror("Error",f"Due To :{str(errormsg)}",parent=self.master)    



    def fetch_data(self):
        student_id = self.var_id.get()
        conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        my_cursor = conn.cursor()

        # Modify the SQL query to filter data for a specific student
        query = "SELECT * FROM student WHERE id = %s"
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
        self.var_photo.set(data[12]),

        self.var_deg.set(data[13]),
        self.var_graduYear.set(data[14]),
        self.var_cgpa.set(data[15]),
        self.var_awards.set(data[16]),
        self.var_projTitle.set(data[17]),
        self.var_projDesc.set(data[18]),
        self.var_projGrade.set(data[19]),
        self.var_internCom.set(data[20]),
        self.var_internDur.set(data[21]),
        self.var_internRole.set(data[22]),
        self.var_extraCurri.set(data[23]),




    #========Function to update data========== 
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.master)
        else:

            #id = self.var_id.get()
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
                Upadte=messagebox.askyesno("Update","Do you want to update this student details",parent=self.master)
                if Upadte>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year1=%s,sem=%s,sname=%s,usn=%s,gender=%s,email=%s,phone=%s,paddress=%s,taddress=%s,photo=%s,deg=%s,graduYear=%s,cgpa=%s,awards=%s,projTitle=%s,projDesc=%s,projGrade=%s,internCom=%s,internDur=%s,internRole=%s,extraCurri=%s where id=%s",(

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
                                                                                                                self.var_deg.get(),
                                                                                                                self.var_graduYear.get(),
                                                                                                                self.var_cgpa.get(),
                                                                                                                self.var_awards.get(),
                                                                                                                self.var_projTitle.get(),
                                                                                                                self.var_projDesc.get(),
                                                                                                                self.var_projGrade.get(),
                                                                                                                self.var_internCom.get(),
                                                                                                                self.var_internDur.get(),
                                                                                                                self.var_internRole.get(),
                                                                                                                self.var_extraCurri.get(),
                                                                                                                self.var_id.get()
                                                                                                                ))
                else:
                    if not Upadte:
                        return
                messagebox.showinfo("Success","Student info Succesfully updated",parent=self.master)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as ES:
                messagebox.showerror("Error",f"Due To:{str(ES)}",parent=self.master)



    #========Functions to Validate data========== 


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
        if len(phone_number) != 10:
            return False
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
            messagebox.showerror("Error","Student id must be required",parent=self.master)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.master)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",passwd="aDmin@321",database="student_data")
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student info Succesfully deleted",parent=self.master)
            except Exception as ES:
                messagebox.showerror("Error",f"Due To:{str(ES)}",parent=self.master)


    #========Function to delete data========== 
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        #self.var_id.set("")
        self.var_name.set("")
        self.var_usn.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_paddress.set("")
        self.var_taddress.set("")
        self.var_photo.set("")

        self.var_deg.set("Select Degree")
        self.var_graduYear.set("")
        self.var_cgpa.set("")
        self.var_awards.set("")
        self.var_projTitle.set("")
        self.var_projDesc.set("")
        self.var_projGrade.set("")
        self.var_internCom.set("")
        self.var_internDur.set("")
        self.var_internRole.set("")
        self.var_extraCurri.set("")

    
        
if __name__=="__main__":
    master=ThemedTk(theme="clam")
    obj=student_info(master)
    master.mainloop() 






    