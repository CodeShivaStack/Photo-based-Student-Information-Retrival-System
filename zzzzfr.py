import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone
from tkinter import *
import mysql.connector
import ctypes

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
from tkinter import messagebox


class face_rec:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=90)

        # bg_image
        img = Image.open(r"resources\23.png")
        img = img.resize((1530, 710), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=90, width=1530, height=320)

        b1 = Button(self.root, text="Face Recognize", command=self.face_recognize, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1.place(x=0, y=400, width=1530, height=65)

        img1 = Image.open(r"resources\22.png")
        img1 = img1.resize((1530, 710), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img1 = Label(self.root, image=self.photoimg1)
        bg_img1.place(x=0, y=465, width=1530, height=320)

    # def show_more_details(self, details):
    #     detail_window = Toplevel(self.root)
    #     detail_window.geometry("400x400")
    #     detail_window.title("More Details")
        
    #     text = Text(detail_window)
    #     text.insert(END, details)
    #     text.pack()



    def show_more_details(self, student_id):
        conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
        my_cursor = conn.cursor()
        
        # Fetch all details of the student
        my_cursor.execute("SELECT * FROM student_info WHERE id=%s", (student_id,))
        details = my_cursor.fetchone()
        
        if details:
            column_names = [desc[0] for desc in my_cursor.description]
            detail_text = "\n".join([f"{column}: {value}" for column, value in zip(column_names, details)])
        else:
            detail_text = "No details found for this student."
        
        conn.close()

        detail_window = Toplevel(self.root)
        detail_window.geometry("400x400")
        detail_window.title("More Details")

        text = Text(detail_window)
        text.insert(END, detail_text)
        text.configure(state=DISABLED)
        text.pack()



    def face_recognize(self):
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        imgBackground = cv2.imread("resources/444.png")
        imgBackground_resized = cv2.resize(imgBackground, (screen_width, int(screen_width / imgBackground.shape[1] * imgBackground.shape[0])))

        floderModePath = 'resources/Modes'
        modePathList = os.listdir(floderModePath)
        imgModeList = [cv2.imread(os.path.join(floderModePath, path)) for path in modePathList]

        print("Loading Encoded File...")
        with open("EncodeFile.p", "rb") as file:
            encodeListKnown, studentIds = pickle.load(file)
        print("Encoded File Loaded...")

        modeType = 0
        counter = 0

        while True:
            success, img = cap.read()

            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

            imgBackground_resized[250:250 + 480, 120:120 + 640] = img
            img = cv2.resize(img, (380, 640))

            imgMode_resized = cv2.resize(imgModeList[1], (651, 860))
            imgBackground_resized[2:2 + 860, 883:883 + 651] = imgMode_resized

            if encodeCurFrame:
                for encoFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                    matches = face_recognition.compare_faces(encodeListKnown, encoFace)
                    faceDis = face_recognition.face_distance(encodeListKnown, encoFace)
                    matchIndex = np.argmin(faceDis)

                    if matches[matchIndex]:
                        print("Known Face Was Detected")

                        id = studentIds[matchIndex]
                        y1, x2, y2, x1 = faceLoc
                        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                        bbox = 120 + x1, 265 + y1, x2 - x1, y2 - y1
                        imgBackground = cvzone.cornerRect(imgBackground_resized, bbox, rt=0)

                        conn = mysql.connector.connect(host="localhost", user="root", passwd="aDmin@321", database="student_data")
                        my_cursor = conn.cursor()

                        my_cursor.execute("select name from student_info where id=" + str(id))
                        n = my_cursor.fetchone()
                        n = "+".join(n) if n else "Unknown"

                        my_cursor.execute("select usn from student_info where id=" + str(id))
                        u = my_cursor.fetchone()
                        u = "+".join(u) if u else "Unknown"

                        my_cursor.execute("select dep from student_info where id=" + str(id))
                        d = my_cursor.fetchone()
                        d = "+".join(d) if d else "Unknown"

                        my_cursor.execute("select gender from student_info where id=" + str(id))
                        g = my_cursor.fetchone()
                        g = "+".join(g) if g else "Unknown"
                        G = "He" if g == "Male" else "She" if g else "Unknown"

                        my_cursor.execute("select email from student_info where id=" + str(id))
                        e = my_cursor.fetchone()
                        e = "+".join(e) if e else "Unknown"

                        my_cursor.execute("select phone from student_info where id=" + str(id))
                        p = my_cursor.fetchone()
                        p = "+".join(map(str, p)) if p else "Unknown"

                        image_path = f"images/{studentIds[matchIndex]}.jpg"
                        if not os.path.exists(image_path):
                            image_path = f"images/{studentIds[matchIndex]}.png"
                        if not os.path.exists(image_path):
                            image_path = f"images/{studentIds[matchIndex]}.jpeg"

                        imgStudent = cv2.imread(image_path) if os.path.exists(image_path) else None
                        if imgStudent is None:
                            print("Error: Image not found or cannot be read.")
                            exit()

                        region_height, region_width, _ = imgBackground_resized[191:191+160, 949:949+160].shape
                        imgStudent_resized = cv2.resize(imgStudent, (region_width, region_height))
                        imgBackground_resized[191:191+region_height, 949:949+region_width] = imgStudent_resized

                        cv2.putText(imgBackground_resized, f"{n}", (1120, 430), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{u}", (1120, 485), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{d}", (1120, 540), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{id}", (1120, 595), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{g}", (1120, 650), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{e}", (1120, 705), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{p}", (1120, 760), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                        cv2.putText(imgBackground_resized, f"{G} is Our Student", (1160, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

                        details = f"Name: {n}\nUSN: {u}\nDepartment: {d}\nID: {id}\nGender: {g}\nEmail: {e}\nPhone: {p}"
                        show_more_button = Button(self.root, text="Show More", command=lambda: self.show_more_details(id), font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
                        show_more_button.place(x=1200, y=760)

                    else:
                        imgMode_resized = cv2.resize(imgModeList[2], (651, 860))
                        imgBackground_resized[2:2 + 860, 883:883 + 651] = imgMode_resized
            else:
                imgMode_resized = cv2.resize(imgModeList[0], (651, 860))
                imgBackground_resized[2:2 + 860, 883:883 + 651] = imgMode_resized

            cv2.imshow("Student", imgBackground_resized)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = face_rec(root)
    root.mainloop()
