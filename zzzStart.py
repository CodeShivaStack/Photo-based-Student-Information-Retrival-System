from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Slogin import SLoginWindow
from Alogin import LoginWindow


class PBSIR_System:
    def __init__(self, master):
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


        #studentLogin_button
        img1=Image.open(r"resources/21.png")
        img1=img1.resize((1530,710),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(self.master,image=self.photoimg1,command=self.Slogin,cursor="hand2")
        b1.place(x=200,y=100,width=520,height=220)

        b1=Button(self.master,text="Student Login",command=self.Slogin,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b1.place(x=200,y=300,width=520,height=40)

        #adminLogin_button
        img2=Image.open(r"resources/24.png")
        img2=img2.resize((1530,710),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(self.master,command=self.Alogin,image=self.photoimg2,cursor="hand2")
        b2.place(x=800,y=100,width=520,height=220)

        b2=Button(self.master,command=self.Alogin,text="Admin Login",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b2.place(x=800,y=300,width=520,height=40)



    #====Function Buttons====
    def Slogin(self):
        self.new_window=Toplevel(self.master)
        self.app=SLoginWindow(self.new_window)  


    def Alogin(self):
        self.new_window=Toplevel(self.master)
        self.app=LoginWindow(self.new_window)




if __name__=="__main__":
    master=Tk()
    obj=PBSIR_System(master)
    master.mainloop()   