from tkinter import *
from tkinter import filedialog
import cv2
import os

root = Tk()
root.geometry("300x260")
root.title("Frame Generator")

def dest():                                                                                 #Function defined for selecting destination folder button
    global x                                                                                #Global variable for assigning folder path

    folder_Selected=filedialog.askdirectory(initialdir="/",title="Select destination folder")

    print(folder_Selected)
    x=folder_Selected
    my_label.config(text=x)

def video():                                                                                 #Function defined for selecting video path button
    global y                                                                                 #Global variable for assigning video file path

    root.filename = filedialog.askopenfilename(initialdir="/", title="Select video file")

    print(root.filename)
    y=root.filename

    try:
        if(os.path.splitext(y)[-1].lower()==".mp4"):
            my_label2.config(text=y)
            label_x.config(text="")
        else:
            label_x.config(text="Select valid file(.mp4)")                                      #GUI label for invalid path
            print("Select valid file(.mp4)")

    except:
        print("Select valid file(.mp4) ")


def generate():                                                                                 #Function defined for generating frames
    try:                                                                                        #Try and Exception block for empty input
        videocap = cv2.VideoCapture(y)                                                          #using cv2 module for capturing video
        count = 0
        while True:
            success, image = videocap.read()
            if success == False:
                videocap.release()
                break

            cv2.imwrite(f"{x}\Frame{count}.jpg", image)                                          #Saving frames to the specified location
            print('Read a new frame: ', success)
            count += 1

        os.startfile(x)                                                                           #after generating frames, jumping to the destination folder for viewing frames
    except NameError or UnboundLocalError as ex:

        Label(root, text="video file path or destination"+"\n"+" folder path not selected", font=('Aerial 11')).pack()
        print("video file path or destination"+"\n"+"folder path not selected")



my_btn=Button(root,text="Browse video file",command=video).pack(padx=10,pady=10)                #Button for browsing files for selecting input video file
my_label2=Label(root, text="", font=('Aerial 11'))
my_label2.pack()

my_btn=Button(root,text="Browse frame destination folder",command=dest).pack()                  #Button for browsing files for selecting destination folder
my_label=Label(root, text="", font=('Aerial 11'))
my_label.pack()

my_btn=Button(root, text="Generate frames", command=generate).pack()                            #Button for final submission
label_x=Label(root, text="", font=('Aerial 11'))
label_x.pack()

root.mainloop()
