from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Slogin import SLoginWindow
from Start1 import StartPBSIR_System


class PBSIR_System:
    def __init__(self, master):
        self.master=master
        self.master.geometry("1530x790+0+0")
        self.master.title("Photo based Student Information Retrival System")
        
        # bg_image
        img=Image.open(r"resources/001.png")
        img=img.resize((1530,790),Image.LANCZOS)
        
        self.photoimg=ImageTk.PhotoImage(img)


        bg_img=Label(self.master,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)



        #Start_button
        img2=Image.open(r"resources/Buttons/StartBtn.png")
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(self.master,command=self.Start1,image=self.photoimg2,cursor="hand2",border=0)
        b2.place(x=670,y=365)



    #====Function Buttons====
    def Start1(self):
        self.new_window=Toplevel(self.master)
        self.app=StartPBSIR_System(self.new_window)




if __name__=="__main__":
    master=Tk()
    obj=PBSIR_System(master)
    master.mainloop()   