import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
import math
from turtle import width

def TemaOscuro(*args):
    estilos.configure("mainframe.TFrame", background="#010924")
    estilos_label1.configure("Label1.TLabel", background="#010924", foreground="white")
    estilos_label2.configure("Label2.TLabel", background="#010924", foreground="white")
    estilos_botones_numeros.configure("Botones_numeros.TButton", background="#00044A", foreground="#FFFFFF")
    estilos_botones_numeros.map("Botones_numeros.TButton", background=[("active","#020A90")])
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#00044A", foreground="#FFFFFF")
    estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active","#000AB1")])
    estilos_botones.configure("Botones.TButton", background="#010924", foreground="#FFFFFF")
    estilos_botones.map("Botones.TButton", background=[("active","#000AB1")])

def TemaClaro(*args):
    estilos.configure("mainframe.TFrame", background="#DBDBDB", foreground="black")
    estilos_label1.configure("Label1.TLabel", background="#DBDBDB", foreground="black")
    estilos_label2.configure("Label2.TLabel", background="#DBDBDB", foreground="black")
    estilos_botones_numeros.configure("Botones_numeros.TButton", background="white", foreground="black")
    estilos_botones_numeros.map("Botones_numeros.TButton", background=[("active","#B9B9B9")], foreground=[("active","white")])
    estilos_botones_borrar.configure("Botones_borrar.TButton", background="#CECECE", foreground="black")
    estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active","#FF0000")], foreground=[("active","white")])
    estilos_botones.configure("Botones.TButton", background="#CECECE", foreground="black")
    estilos_botones.map("Botones.TButton", background=[("active","#858585")], foreground=[("active","white")])

root = Tk()
root.title("Calculadora")
# root.title("Población futura")
root.geometry("+500+80")
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)


estilos = Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background="#DBDBDB")

mainframe = Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0,row=0, sticky=(W,N,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

# estilos label 
estilos_label1 = Style()
estilos_label1.configure("Label1.TLabel", font="arial 15", anchor="E")

estilos_label2 = Style()
estilos_label2.configure("Label2.TLabel", font="arial 40", anchor="E")


entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0,row=0, columnspan=4, sticky=(W,N,E,S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0,row=1, columnspan=4, sticky=(W,N,E,S))

# estilos botones 
estilos_botones_numeros = Style()
estilos_botones_numeros.configure("Botones_numeros.TButton", font="arial 22", width="5", background="#FFFFFF", relief="flat")
estilos_botones_numeros.map("Botones_numeros.TButton", foreground=[("active","#B9B9B9")])
estilos_botones_borrar = Style()
estilos_botones_borrar.configure("Botones_borrar.TButton", font="arial 22", width="5", background="#CECECE", relief="flat")
estilos_botones_borrar.map("Botones_borrar.TButton", background=[("active","#FF0000")], foreground=[("active","white")])
estilos_botones = Style()
estilos_botones.configure("Botones.TButton", font="arial 22", width="5", background="#CECECE", relief="flat")
estilos_botones.map("Botones.TButton", foreground=[("active","#858585")])


button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton")
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton")
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton")
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton")
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton")
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton")
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton")
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton")
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton")
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton")

button_borrar = ttk.Button(mainframe, text=chr(9003), style="Botones_borrar.TButton")
button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton")
button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones.TButton")
button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones.TButton")
button_punto = ttk.Button(mainframe, text=".", style="Botones.TButton")

button_division = ttk.Button(mainframe, text=chr(247), style="Botones.TButton")
button_multiplicacion = ttk.Button(mainframe, text="x", style="Botones.TButton")
button_resta = ttk.Button(mainframe, text="-", style="Botones.TButton")
button_suma = ttk.Button(mainframe, text="+", style="Botones.TButton")
button_igual = ttk.Button(mainframe, text="=", style="Botones.TButton")
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="Botones.TButton")


# graficar 
button_parentesis1.grid(column=0,row=2, sticky=(W,N,E,S))
button_parentesis2.grid(column=1,row=2, sticky=(W,N,E,S))
button_borrar_todo.grid(column=2,row=2, sticky=(W,N,E,S))
button_borrar.grid(column=3,row=2, sticky=(W,N,E,S))

button7.grid(column=0,row=3, sticky=(W,N,E,S))
button8.grid(column=1,row=3, sticky=(W,N,E,S))
button9.grid(column=2,row=3, sticky=(W,N,E,S))
button_division.grid(column=3,row=3, sticky=(W,N,E,S))

button4.grid(column=0,row=4, sticky=(W,N,E,S))
button5.grid(column=1,row=4, sticky=(W,N,E,S))
button6.grid(column=2,row=4, sticky=(W,N,E,S))
button_multiplicacion.grid(column=3,row=4, sticky=(W,N,E,S))

button1.grid(column=0,row=5, sticky=(W,N,E,S))
button2.grid(column=1,row=5, sticky=(W,N,E,S))
button3.grid(column=2,row=5, sticky=(W,N,E,S))
button_suma.grid(column=3,row=5, sticky=(W,N,E,S))

button0.grid(column=0,row=6,columnspan=2, sticky=(W,N,E,S))
button_punto.grid(column=2,row=6, sticky=(W,N,E,S))
button_resta.grid(column=3,row=6, sticky=(W,N,E,S))

button_igual.grid(column=0,row=7,columnspan=3, sticky=(W,N,E,S))
button_raiz_cuadrada.grid(column=3,row=7, sticky=(W,N,E,S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind("<KeyPress-o>", TemaOscuro)
root.bind("<KeyPress-c>", TemaClaro)

root.mainloop()