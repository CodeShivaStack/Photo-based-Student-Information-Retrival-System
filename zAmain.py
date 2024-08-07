from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from zAStudentDetails import student_info
from about import aboutus
from encodegen import encodeGene
from faceRec import face_rec


class PBSIR_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Photo based Student Information Retrival System")
        
        # bg_image
        img=Image.open(r"resources/intro.png")
        img=img.resize((1530,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(self.root,text="Photo-based Student Information Retrival System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=105)


        #student_button
        img1=Image.open(r"resources/21.png")
        img1=img1.resize((1530,710),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(self.root,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1=Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b1.place(x=200,y=300,width=220,height=40)


        #Train_data
        img2=Image.open(r"resources/22.png")
        img2=img2.resize((1530,710),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(self.root,image=self.photoimg2,command=self.encodeGen,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1=Button(self.root,text="Train Data",command=self.encodeGen,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b1.place(x=500,y=300,width=220,height=40)


        #Face_detection_button
        img3=Image.open(r"resources/23.png")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(self.root,command=self.facerec,image=self.photoimg3,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3=Button(self.root,command=self.facerec,text="Face Detection",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b3.place(x=800,y=300,width=220,height=40)


        #AboutUs
        img4=Image.open(r"resources/24.png")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(self.root,command=self.about,image=self.photoimg4,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4=Button(self.root,command=self.about,text="About Us",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b4.place(x=1100,y=300,width=220,height=40)



    #====Function Buttons====
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student_info(self.new_window)

    def encodeGen(self):
        self.new_window=Toplevel(self.root)
        self.app=encodeGene(self.new_window)    

    def facerec(self):
        self.new_window=Toplevel(self.root)
        self.app=face_rec(self.new_window)

    def about(self):
        self.new_window=Toplevel(self.root)
        self.app=aboutus(self.new_window)




if __name__=="__main__":
    root=Tk()
    obj=PBSIR_System(root)
    root.mainloop()   