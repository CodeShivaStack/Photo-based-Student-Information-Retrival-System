from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from AStudentDetails import student_info


class aboutus:
    def __init__(self,master):
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


        desc_lbl = Label(self.master, text="Welcome to our Photo-based Student Information Retrival System! Developed as a final year project by our team of four, our mission is to simplify student data access using advanced facial recognition. With a user-friendly interface and robust database integration, our system offers comprehensive student information retrieval. Meet our team members and explore our innovative solution. \n For inquiries, contact us at cs24t11gecm@gmail.com.", font=("times new roman", 16, "bold"), bg="#a4f0ff", fg="#000000",wraplength=1465)
        desc_lbl.place(x=55, y=140)

        desc_lbl1 = Label(self.master, text="Developed by our team of four!!", font=("times new roman", 16, "bold"), bg="#a4f0ff", fg="#000000")
        desc_lbl1.place(x=0, y=240,width=1530,height=50)


        developer1_lbl=Label(bg_img,text="PRAKRUTHI H K",font=("times new roman",20,"bold"),bg="#a4f0ff", fg="#000000")
        developer1_lbl.place(x=90,y=200,width=250,height=50)

        developer2_lbl=Label(bg_img,text="SHIVARADDI R M",font=("times new roman",20,"bold"),bg="#a4f0ff", fg="#000000")
        developer2_lbl.place(x=480,y=200,width=240,height=50)

        developer3_lbl=Label(bg_img,text="INDUSHREE K T",font=("times new roman",20,"bold"),bg="#a4f0ff", fg="#000000")
        developer3_lbl.place(x=850,y=200,width=250,height=50)

        
        developer4_lbl=Label(bg_img,text="SAVITRI H G",font=("times new roman",20,"bold"),bg="#a4f0ff", fg="#000000")
        developer4_lbl.place(x=1220,y=200,width=200,height=50)

        

    



if __name__=="__main__":
    master=Tk()
    obj=aboutus(master)
    master.mainloop()   