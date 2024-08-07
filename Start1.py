from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Slogin import SLoginWindow
from Alogin import LoginWindow


class StartPBSIR_System:
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
        img1=Image.open(r"resources/Buttons/StudLogin.png")
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(self.master,command=self.Slogin,image=self.photoimg1,cursor="hand2",border=0)
        b1.place(x=630,y=150)


        #adminLogin_button
        img2=Image.open(r"resources/Buttons/AdminLogin.png")
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(self.master,command=self.Alogin,image=self.photoimg2,cursor="hand2",border=0)
        b2.place(x=630,y=275)



    #====Function Buttons====
    def Slogin(self):
        self.new_window=Toplevel(self.master)
        self.app=SLoginWindow(self.new_window)  


    def Alogin(self):
        self.new_window=Toplevel(self.master)
        self.app=LoginWindow(self.new_window)




if __name__=="__main__":
    master=Tk()
    obj=StartPBSIR_System(master)
    master.mainloop()   