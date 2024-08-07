import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
from tkinter import *
import mysql.connector
import ctypes


from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from ttkthemes import ThemedTk
from tkinter import messagebox



class face_rec:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lbl=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=90)
        
        # bg_image
        img=Image.open(r"resources\23.png")
        img=img.resize((1530,710),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=90,width=1530,height=320)

        b1=Button(self.root,text="Face Recognize",command=self.face_recognize,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white") 
        b1.place(x=0,y=400,width=1530,height=65)

  

        img1=Image.open(r"resources\22.png")
        img1=img1.resize((1530,710),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img1=Label(self.root,image=self.photoimg1)
        bg_img1.place(x=0,y=465,width=1530,height=320)

    def face_recognize(self):
        # Get screen resolution
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        cap = cv2.VideoCapture(0)

        cap.set(3, 640)
        cap.set(4, 480)

        imgBackground = cv2.imread("resources/444.png")

        # Resize background image to fit the screen while maintaining aspect ratio
        imgBackground_resized = cv2.resize(imgBackground, (screen_width, int(screen_width / imgBackground.shape[1] * imgBackground.shape[0])))


        #IMPORT MODE IMAGES
        floderModePath = 'resources/Modes'
        modePathList = os.listdir(floderModePath)
        imgModeList = []
        for path in modePathList:
            imgModeList.append(cv2.imread(os.path.join(floderModePath, path)))
        #print(len(imgModeList))
        # imgModeList[0].shape = (1080,820,3) 

        #Load Encoding File
        print("Loading Encoded File...")
        file = open("EncodeFile.p", "rb")
        encodeListKnownIds = pickle.load(file)
        file.close()
        encodeListKnown, studentIds = encodeListKnownIds
        #print(studentIds)
        print("Encoded File Loaded...")

        modeType = 0
        counter = 0



        while True:
            sucess, img = cap.read()

            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

            imgBackground_resized[250:250 + 480, 120:120  + 640] = img
            img = cv2.resize(img, (380, 640))

            imgMode_resized = cv2.resize(imgModeList[1], (651, 860))

            # Assign the resized mode image to the target region in imgBackground_resized
            imgBackground_resized[2:2 + 860, 883:883 + 651] = imgMode_resized

            
            if encodeCurFrame:

                for encoFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encoFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encoFace)
                    #print("matches", matches)
                    #print("faceDis", faceDis)

                    matchIndex = np.argmin(faceDis)
                    #print("Match Index", matchIndex)

                    if matches[matchIndex]:
                        print("Known Face Was Detected")
                        #print(studentIds[matchIndex])  

                        id = studentIds[matchIndex]
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        bbox = 120 + x1, 265 + y1, x2 - x1, y2 - y1
                        imgBackground = cvzone.cornerRect(imgBackground_resized, bbox, rt = 0)



                        conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
                        my_cursor = conn.cursor()

                        my_cursor.execute("select name from student_info where id=" + str(id))
                        n = my_cursor.fetchone()
                        if n is not None:
                            n = "+".join(n)
                        else:
                            n = "Unknown"

                        my_cursor.execute("select usn from student_info where id=" + str(id))
                        u = my_cursor.fetchone()
                        if u is not None:
                            u = "+".join(u)
                        else:
                            u = "Unknown"

                        my_cursor.execute("select dep from student_info where id=" + str(id))
                        d = my_cursor.fetchone()
                        if d is not None:
                            d = "+".join(d)
                        else:
                            d = "Unknown"

                        my_cursor.execute("select gender from student_info where id=" + str(id))
                        g = my_cursor.fetchone()
                        if g is not None:
                            g = "+".join(g)
                            if g == "Male":
                                G = "He"
                            else:
                                G = "She"
                        else:
                            G = "Unknown"

                        my_cursor.execute("select email from student_info where id=" + str(id))
                        e = my_cursor.fetchone()
                        if e is not None:
                            e = "+".join(e)
                        else:
                            e = "Unknown"

                        my_cursor.execute("select phone from student_info where id=" + str(id))
                        p = my_cursor.fetchone()
                        if p is not None:
                            p = "+".join(map(str, p))
                        else:
                            p = "Unknown"

                                
                        
                        

                        # Path to the image file in your local storage
                        image_path = f"images/{studentIds[matchIndex]}.jpg"
                        # image_path = f"images/400003.png"
                        if os.path.exists(image_path):
                        # Read the image from local storage 
                            imgStudent = cv2.imread(image_path)
                        else:
                            image_path = f"images/{studentIds[matchIndex]}.png"
    
                            if os.path.exists(image_path):    
                            # Read the image from local storage 
                                imgStudent = cv2.imread(image_path)
                            else:
                                image_path = f"images/{studentIds[matchIndex]}.jpeg"
    
                                if os.path.exists(image_path):
                                # Read the image from local storage 
                                    imgStudent = cv2.imread(image_path)
                        

            


                        # Check if the image is successfully loaded
                        if imgStudent is None:
                            print("Error: Image not found or cannot be read.")
                        # Handle the error, maybe exit or continue with default image
                            exit()
                        

                        # Assuming imgBackground_resized is already defined
                        # Define the region to replace in imgBackground_resized
                        region_height, region_width, _ = imgBackground_resized[191:191+160, 949:949+160].shape

                        # Resize imgStudent to match the dimensions of the region in imgBackground_resized
                        imgStudent_resized = cv2.resize(imgStudent, (region_width, region_height))

                        # Replace the region in imgBackground_resized with imgStudent_resized
                        imgBackground_resized[191:191+region_height, 949:949+region_width] = imgStudent_resized

                    
                    
                        cv2.putText(imgBackground_resized, f"{n}", (1120, 430), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{u}", (1120, 485), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{d}", (1120, 540), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                        cv2.putText(imgBackground_resized, f"{id}", (1120, 595), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{g}", (1120, 650), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{e}", (1120, 705), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{p}", (1120, 760), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                        # (w, h), _ = cv2.getTextSize(f"{G} is Over Student ", cv2.FONT_HERSHEY_COMPLEX, 1, 2)
                        # offset = 414-w//2
                        # cv2.putText(imgBackground_resized, f"{G} is Over Student ", (1120 + offset, 370), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                        cv2.putText(imgBackground_resized, f"{G} is Our Student ", (1160, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        #cv2.putText(imgBackground_resized, f"Student Detected!!", (1167, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        #cv2.putText(imgBackground_resized, f"{G} is Our Student ", (280, 205), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                    else:
                        imgMode_resized = cv2.resize(imgModeList[2], (651, 860))

                        # Assign the resized mode image to the target region in imgBackground_resized
                        imgBackground_resized[2:2 + 860, 883:883 + 651] = imgMode_resized

            else:
                imgMode_resized = cv2.resize(imgModeList[0], (651, 860))

                # Assign the resized mode image to the target region in imgBackground_resized
                imgBackground_resized[2:2 + 860, 883:883 + 651] = imgMode_resized

                # cv2.putText(imgBackground_resized, f"NO Face Detected!!", (1167, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                # cv2.putText(imgBackground_resized, f"NO Face Detected!!", (280, 205), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                # Uncondition = 1


            #cv2.imshow("Student", img)
                    
            cv2.imshow("Student", imgBackground_resized)
                    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=face_rec(root)
    root.mainloop()  