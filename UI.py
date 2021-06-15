# importing libraries
import tkinter as tk
from tkinter import ttk
import cv2
import os
from tkinter import filedialog
import numpy as np
from os import listdir
from os.path import isfile, join

window = tk.Tk()
window.title("Face_Recogniser")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(
    window, text="Family Member Face-Recognition-System", font=('times', 20, 'bold'))

message.place(x=650, y=10)


lbl1 = tk.Label(window, text="Add a New Member", font=('times', 15, ' bold '))
lbl1.place(x=800, y=100)


lbl2 = tk.Label(window, text="Enter Name of Member:", font=('times', 12, ' bold '))
lbl2.place(x=10, y=150)

txt2 = tk.Entry(window, width=20,
                bg="white", fg="blue",
                font=('times', 15, ' bold '))
txt2.place(x=10, y=200)

lbl4 = tk.Label(window, text="Recognize a Member", font=('times', 15, ' bold '))
lbl4.place(x=800, y=300)

lbl3 = tk.Label(window, text="Recognize from an Image:", font=('times', 12, ' bold '))
lbl3.place(x=10, y=350)

lbl5 = tk.Label(window, text="Use Cam:", font=('times', 12, ' bold '))
lbl5.place(x=10, y=450)

lbl7 = tk.Label(window, text="Search Folder for a Member Image:", font=('times', 12, ' bold '))
lbl7.place(x=10, y=550)

lbl6 = tk.Label(window, text="Member Name:", font=('times', 12, ' bold '))
lbl6.place(x=10, y=600)

txt3 = tk.Entry(window, width=20,
                bg="white", fg="blue",
                font=('times', 12, ' bold '))
txt3.place(x=10, y=650)

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def searchAllPic():
    dirPath = filedialog.askdirectory()
    data_path = txt3.get() + '/'
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    Training_Data, Labels = [], []

    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    Labels = np.asarray(Labels, dtype=np.int32)

    model = cv2.face.LBPHFaceRecognizer_create()

    model.train(np.asarray(Training_Data), np.asarray(Labels))

    print("Model Training Complete!!!!!")

    onlyfiles = [f for f in listdir(dirPath) if isfile(join(dirPath, f))]
    for files in onlyfiles:
        files = dirPath + '/' + files
        img = cv2.imread(files)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        if faces is ():
            return img, []

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi = img[y:y + h, x:x + w]
            roi = cv2.resize(roi, (200, 200))
            try:
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                result = model.predict(roi)
                if result[1] < 500:
                    confidence = int(100 * (1 - (result[1]) / 300))
                    display_string = str(confidence) + '% Confidence it is user'
                    # cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)

                    if confidence > 80:
                        cv2.putText(img, "Farzaib", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow('Face Cropper', img)
                        cv2.waitKey(0)
                        print('true')
                    # else:
                    #     cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                    #     cv2.imshow('Face Cropper', image)
                    #     print('false')
            except:
                cv2.putText(img, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                cv2.imshow('Face Cropper', img)
                pass



def face_detector2(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))

    return img, roi


def recognizeInImage():

    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                          filetype=(("jpeg", "*.jpg"), ("All Files", "*.*")))
    f = open("users.txt", "r")
    for user in f:
        user = user[0:len(user)-1]
        data_path = user + '/'
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

        Training_Data, Labels = [], []

        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)

        Labels = np.asarray(Labels, dtype=np.int32)

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data), np.asarray(Labels))

        print("Model Training Complete!!!!!")

        frame = cv2.imread(filename)
        image, face = face_detector2(frame)

        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = model.predict(face)

            if result[1] < 500:
                confidence = int(100 * (1 - (result[1]) / 300))

                if confidence > 83:
                    cv2.putText(image, user, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('Face Cropper', image)
                    print('true')
                    break
        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass

    cv2.imshow('Face Cropper', image)
    cv2.waitKey(0)


def recognizefromWebcam():
    videoStreamObject = cv2.VideoCapture(0)
    cap, frame = videoStreamObject.read()
    f = open("users.txt", "r")
    for user in f:
        user = user[0:len(user)-1]
        data_path = user + '/'
        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

        Training_Data, Labels = [], []

        for i, files in enumerate(onlyfiles):
            image_path = data_path + onlyfiles[i]
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images, dtype=np.uint8))
            Labels.append(i)

        Labels = np.asarray(Labels, dtype=np.int32)

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data), np.asarray(Labels))

        print("Model Training Complete!!!!!")

        image, face = face_detector2(frame)

        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = model.predict(face)

            if result[1] < 500:
                confidence = int(100 * (1 - (result[1]) / 300))

                if confidence > 83:
                    cv2.putText(image, user, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('Face Cropper', image)
                    print('true')
                    break
        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass

    cv2.imshow('Face Cropper', image)
    cv2.waitKey(0)
    videoStreamObject.release()


def face_extractor(img):
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]

    return cropped_face


def createUser():
    cap = cv2.VideoCapture(0)
    count = 0
    name = txt2.get()
    path = os.getcwd()
    path = path + '/' + name
    os.mkdir(path)
    with open("users.txt", "a") as file_object:
        file_object.write(name + '\n')
    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = name + '/u' + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)

            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
        else:
            print("Face not Found")
            pass

        if cv2.waitKey(1) == 13 or count == 125:
            break

    cap.release()
    cv2.destroyAllWindows()
    print('Colleting Samples Complete!!!')


def say():
    print('Hello')

trainImg = tk.Button(window, text="Add Member", fg="white", bg="blue",
                     command=createUser, activebackground="Red",
                     font=('times', 12, ' bold '))
trainImg.place(x=10, y=250)

browseImg = tk.Button(window, text="Browse an Image", fg="white", bg="blue",
                     command=recognizeInImage, activebackground="Red",
                     font=('times', 12, ' bold '))
browseImg.place(x=10, y=400)

camImg = tk.Button(window, text="Image from Cam", fg="white", bg="blue",
                     command=recognizefromWebcam, activebackground="Red",
                     font=('times', 12, ' bold '))
camImg.place(x=10, y=500)

searchImg = tk.Button(window, text="Search From Folder", fg="white", bg="blue",
                     command=searchAllPic, activebackground="Red",
                     font=('times', 12, ' bold '))
searchImg.place(x=10, y=700)

quitWindow = tk.Button(window, text="Quit",
                       command=window.destroy, fg="white", bg="blue", activebackground="Red",
                       font=('times', 15, ' bold '))
quitWindow.place(x=1400, y=800)

window.mainloop()


