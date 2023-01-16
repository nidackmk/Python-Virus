import threading
import cv2
from tkinter import *

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def thread_function2():
    for i in range(1, 2):
        window = Tk()
        window.title("Virüss")
        Label(window, text="Şifreyi biliyorsan çıkmak çok kolayyyy", font="Verdana 12", bg="red", fg="white").pack()
        window.mainloop()

        window2 = Tk()
        window2.title("Virüss")
        Label(window2, text="Iyyy sen hiç aynaya bakıyor musun puhahahahhaha", font="Verdana 12", bg="red",
              fg="white").pack()
        window2.mainloop()

        window3 = Tk()
        window3.title("Virüss")
        Label(window3, text="Bu yüzünün hali de ne böyle !!!!!", font="Verdana 12", bg="red", fg="white").pack()
        window3.mainloop()

        window4 = Tk()
        window4.title("Virüss")
        Label(window4, text="Yoksa Şifreyi bilmiyor musun?!!!!", font="Verdana 12", bg="red", fg="white").pack()
        window4.mainloop()

        window5 = Tk()
        window5.title("Virüss")
        Label(window5, text="O halse burdan asla çıkamayacksınnnn!!!!!!!!!!", font="Verdana 12", bg="red",
              fg="white").pack()
        window5.mainloop()


thread2 = threading.Thread(target=thread_function2)

thread2.start()

while 1:
    ret, frame = cap.read()
    if ret:
        """görüntünün y eksenine göre yansımasını aldık"""
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray4 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Webcam2", gray2)
        cv2.imshow("Webcam3", gray3)
        cv2.imshow("Webcam1", gray)
        cv2.imshow("Webcam4", gray4)
        cv2.imshow("Webcam", frame)

        if cv2.waitKey(100) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
