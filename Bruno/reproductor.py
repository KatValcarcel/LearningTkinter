import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY)
# b1.pack(side=LEFT, padx=5, pady=5)

from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

root = ttk.Window()
root.title("Bruno")
root.geometry("+500+80")
# root = ttk.Window(themename="superhero")

def reproducir():
    global cap
    if cap is not None:
        ret,frame=cap.read()
        if ret == True:
            frame =imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im=Image.fromarray(frame)
            img=ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image=img
            lblVideo.after(10, reproducir)
        else:
            lblInfoPath.configure(text='Seleccione otro video', foreground="blue")
            lblVideo.image=''
            cap.release()

def elegir_ver():
    global cap

    video_path= filedialog.askopenfilename(filetypes=[
        ('all video format','.mp4'),
        ('all video format','.avi'),
        ('all video format','.mov'),
    ])
    if len(video_path)>0:
        lblInfoPath.configure(text=video_path, foreground="blue")
        cap=cv2.VideoCapture(video_path)
        reproducir()
    else:
        lblInfoPath.configure(text='Aún no se ha seleccionado un video', foreground="red")

btnVer = ttk.Button(root, text='Elegir y ver video', command=elegir_ver)
btnVer.grid(column=0,row=0, pady=5,padx=5, columnspan=2)

lblInfo = ttk.Label(root, text='Video:', bootstyle="dark")
lblInfo.grid(column=0, row=1)

lblInfoPath = ttk.Label(root, text='Aún no se ha seleccionado un video', bootstyle="danger")
lblInfoPath.grid(column=1, row=1)

lblVideo = ttk.Label(root)
lblVideo.grid(column=0, row=2,columnspan=2)

root.mainloop()
