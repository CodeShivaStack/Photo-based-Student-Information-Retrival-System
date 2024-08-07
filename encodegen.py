import cv2
import face_recognition
import pickle
import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from ttkthemes import ThemedTk
from tkinter import messagebox



class encodeGene:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1530x790+0+0")
        self.master.title("Photo based Student Information Retrival System")

        title_lbl=Label(self.master,text="Training Data Set",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=90)
        
        # bg_image
        img=Image.open(r"resources\23.png")
        img=img.resize((1530,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.master,image=self.photoimg)
        bg_img.place(x=0,y=90,width=1530,height=320)

        b1=Button(self.master,text="Encode Student Images",command=self.startEncodings,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b1.place(x=0,y=400,width=1530,height=65)



        img1=Image.open(r"resources\22.png")
        img1=img1.resize((1530,710),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img1=Label(self.master,image=self.photoimg1)
        bg_img1.place(x=0,y=465,width=1530,height=320)


        

   
    def findEncodings(self, imagesList):
        encodeList = []
        for img in imagesList:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)

        return encodeList
    
    def startEncodings(self):

        folderPath = 'images'
        pathList = os.listdir(folderPath)
        print(pathList)
        imgList = []
        studentIds = []
        for path in pathList:
            imgList.append(cv2.imread(os.path.join(folderPath, path)))
            studentIds.append(os.path.splitext(path)[0])
            #print(path)
            #print(os.path.splitext(path)[0])
        print(studentIds)

        #messagebox.showinfo("Encoding Started...","Encoding Started...")
        # title_lbl1=Label(self.master,text="Encoding Started...",font=("times new roman",35,"bold"),bg="white",fg="red")
        # title_lbl1.place(x=0,y=200,width=1530,height=90)
        print("Encoding Started...")
        encodeListKnown = self.findEncodings(imgList)
        encodeListKnownIds = [encodeListKnown, studentIds]
        #print(encodeListKnown)
        print("Encoding Complete")

        file = open("EncodeFile.p", "wb")
        pickle.dump(encodeListKnownIds, file)
        file.close()
        messagebox.showinfo("Result","Dataset Trained Successfully")

if __name__=="__main__":
    master=Tk()
    obj=encodeGene(master)
    master.mainloop()  

# import cv2
# import face_recognition
# import pickle
# import os

# folderPath = 'images'
# pathList = os.listdir(folderPath)
# print(pathList)
# imgList = []
# studentIds = []
# for path in pathList:
#     imgList.append(cv2.imread(os.path.join(folderPath, path)))
#     studentIds.append(os.path.splitext(path)[0])
#     #print(path)
#     #print(os.path.splitext(path)[0])
# print(studentIds)

   
# def findEncodings(imagesList):
#     encodeList = []
#     for img in imagesList:
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         # encode = face_recognition.face_encodings(img)[0]
#         # encodeList.append(encode)
        
#         # Detect faces in the image
#         face_locations = face_recognition.face_locations(imgRGB)
        
#         # Check if any faces are detected
#         if len(face_locations) > 0:
#             # Encode the first face found in the image
#             encode = face_recognition.face_encodings(imgRGB, face_locations)[0]
#             encodeList.append(encode)
#         else:
#             # Handle the case where no faces are detected in the image
#             print("No faces found in the image:", img)

#     return encodeList
# print("Encoding Started...")
# encodeListKnown = findEncodings(imgList)
# encodeListKnownIds = [encodeListKnown, studentIds]
# #print(encodeListKnown)
# print("Encoding Complete")

# file = open("EncodeFile.p", "wb")
# pickle.dump(encodeListKnownIds, file)
# file.close()