import os
import subprocess
import cv2
from time import sleep
from PIL import Image 

def main_app(name):
        
        face_cascade = cv2.CascadeClassifier("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\data\\haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(f"C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\data\\classifiers\\{name}_classifier.xml")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        pred = 0
        while True:
            ret, frame = cap.read()
            #default_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:


                roi_gray = gray[y:y+h,x:x+w]

                id,confidence = recognizer.predict(roi_gray)
                confidence = 100 - int(confidence)
                pred = 0
                if confidence > 50:
                    #if u want to print confidence level
                            #confidence = 100 - int(confidence)
                            pred += +1
                            text = name.upper()
                            font = cv2.FONT_HERSHEY_PLAIN
                            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            frame = cv2.putText(frame, text, (x, y-4), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

                else:   
                            pred += -1
                            text = "UnknownFace"
                            font = cv2.FONT_HERSHEY_PLAIN
                            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                            frame = cv2.putText(frame, text, (x, y-4), font, 1, (0, 0,255), 1, cv2.LINE_AA)

            cv2.imshow("image", frame)


            if cv2.waitKey(10) & 0xFF == ord("q"):
                print(pred)
                if pred > 0 :
                    dim =(150,150 )
                    img = cv2.imread(f"C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\data\\{name}\\{pred}{name}.jpg", cv2.IMREAD_COLOR)
                    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                    cv2.imwrite(f"C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\data\\{name}\\100{name}.jpg", resized)
                    Image1 = Image.open(f"C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\2.png")

                      
                    # make a copy the image so that the  
                    # original image does not get affected 
                    Image1copy = Image1.copy()
                    Image2 = Image.open(f"C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\data\\{name}\\100{name}.jpg")
                    Image2copy = Image2.copy() 
                      
                    # paste image giving dimensions 
                    Image1copy.paste(Image2copy, (200, 120))
                      
                    # save the image  
                    Image1copy.save("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\end.png")
                    frame = cv2.imread("C:\\Users\\riyam\\PycharmProjects\\MajorProject\\FaceRecognition\\end.png", 1)

                    cv2.imshow("Result",frame)
                    subprocess.call(" python C:\\Users\\riyam\\PycharmProjects\\MajorProject\\IDA\\ida.py", shell=True)
                    cv2.waitKey(0)
                break
        cap.release()
        cv2.destroyAllWindows()