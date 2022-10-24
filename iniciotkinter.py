from cProfile import label
import tkinter 
from tkinter import *

ventana = tkinter.Tk()
ventana.title("Tkinter - Demo")
# ancho por alto + coordenadas de ventana
ventana.geometry("600x450+550+150")
#no maximiza
ventana.resizable(width=False, height=False)
# icono 
# ventana.iconbitmap("/path")

# Label(donde, texto, fondo, letra)
label1 = tkinter.Label(ventana, text="Digita algo", bg="black", fg="white", font="Arial 20", width=10)
# graficar
label1.pack(pady=5, fill=tkinter.X)

# textbox 
e_texto= tkinter.Entry(ventana, font="Arial 20")
e_texto.pack()

label_texto = tkinter.Label(ventana)

def mostrarTexto():
    label_texto.pack()

    if e_texto.get()=="":
        label_texto.configure(bg="red", fg="white")
        label_texto["text"]="Aún no escribes nara"
    else:
        label_texto.configure(font="Arial 20")
        label_texto["text"]=e_texto.get()

button1 = tkinter.Button(ventana, text="Ver texto", command=mostrarTexto)
button1.pack()

ventana.mainloop()