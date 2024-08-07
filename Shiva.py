from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from AStudentDetails import student_info


class aboutus:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790+0+0")
        self.master.title("SHIVARADDI R M")
        
        # bg_image
        img=Image.open(r"resources/intro.png")
        img=img.resize((1530,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.master,image=self.photoimg)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(self.master,text="Photo-based Student Information Retrival System",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=105)


        desc_lbl = Label(self.master, text="Welcome to Shivaradi R M profile, here shivaraddi who contributed ui design, datbase backend, face recognition tool", font=("times new roman", 16, "bold"), bg="#a4f0ff", fg="#000000",wraplength=1465)
        desc_lbl.place(x=310, y=140)

        desc_lbl1 = Label(self.master, text="Developed by our team of four!!", font=("times new roman", 16, "bold"), bg="#a4f0ff", fg="#000000")
        desc_lbl1.place(x=0, y=240,width=1530,height=50)



        developer2_lbl=Label(bg_img,text="SHIVARADDI R M",font=("times new roman",20,"bold"),bg="#a4f0ff", fg="#000000")
        developer2_lbl.place(x=640,y=200,width=240,height=50)

        

    



if __name__=="__main__":
    master=Tk()
    obj=aboutus(master)
    master.mainloop()   