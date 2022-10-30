from ast import main
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from turtle import width
from tkinter import messagebox
import math
from math import ceil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# --inicio--
root=Tk()
root.title('Hardy Cross')
root.iconbitmap('C:/Users/katherine/Documents/LearningTkinter/EXE/usmp.ico')
root.geometry('700x450+450+150')

# main frame
main_frame=Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Canvas 
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add ScrollBar to canvas 
my_scrollbar=Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure the canvas 
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
# Another frame inside canvas
second_frame=Frame(my_canvas)
# Add a new frame to a window in the canvas
my_canvas.create_window((0,0),window=second_frame, anchor='nw')


# generar columnas y filas 
second_frame.grid(column=0,row=0, sticky=(W,N,E,S))
for columna in range(12):
    second_frame.columnconfigure(columna, weight=1)

for fila in range(80):
    second_frame.rowconfigure(fila, weight=1)

# estilos
encabezado = Style()
encabezado.configure("encabezado.TLabel", font='arial 10 bold', width='9', anchor='E')

celda=Style()
celda.configure("celda.TLabel", font='arial 10',width='9', anchor='E')

boton =Style()
boton.configure('Boton.TButton', font='arial 10', width='9', background='#003366', refiel='flat')
boton.map('Boton.TButton', foreground=[("active","#001933")])


# TRAMO 2

tramo1lbl = Label(second_frame, text='1 Tramo', style='encabezado.TLabel')
tramo1lbl.grid(column=0, row=2, columnspan=4, sticky=(W,N,E,S))

longlbl1 = Label(second_frame, text='Longitud', style='encabezado.TLabel')
longlbl1.grid(column=0, row=3, sticky=(W,N,E,S))
mlbl1 = Label(second_frame, text='m', style='encabezado.TLabel')
mlbl1.grid(column=1, row=3, sticky=(W,N,E,S))
kmlbl1 = Label(second_frame, text='Km', style='encabezado.TLabel')
kmlbl1.grid(column=2, row=3, sticky=(W,N,E,S))
materiallbl1 = Label(second_frame, text='Material', style='encabezado.TLabel')
materiallbl1.grid(column=3, row=3, sticky=(W,N,E,S))
ABlbl1 = Label(second_frame, text='A-B', style='encabezado.TLabel')
ABlbl1.grid(column=0, row=4, sticky=(W,N,E,S))
BClbl1 = Label(second_frame, text='B-C', style='encabezado.TLabel')
BClbl1.grid(column=0, row=5, sticky=(W,N,E,S))
CDlbl1 = Label(second_frame, text='C-D', style='encabezado.TLabel')
CDlbl1.grid(column=0, row=6, sticky=(W,N,E,S))
DAlbl1 = Label(second_frame, text='D-A', style='encabezado.TLabel')
DAlbl1.grid(column=0, row=7, sticky=(W,N,E,S))

AB_lbl = Entry(second_frame,width='8')
AB_lbl.grid(column=1, row=4)
BC_lbl = Entry(second_frame,width='8')
BC_lbl.grid(column=1, row=5)
CD_lbl = Entry(second_frame,width='8')
CD_lbl.grid(column=1, row=6)
DA_lbl = Entry(second_frame,width='8')
DA_lbl.grid(column=1, row=7)

material_AB_lbl = Entry(second_frame,width='8')
material_AB_lbl.grid(column=3, row=4)
material_BC_lbl = Entry(second_frame,width='8')
material_BC_lbl.grid(column=3, row=5)
material_CD_lbl = Entry(second_frame,width='8')
material_CD_lbl.grid(column=3, row=6)
material_DA_lbl = Entry(second_frame,width='8')
material_DA_lbl.grid(column=3, row=7)

Diamelbl = Label(second_frame, text='Diámetro', style='encabezado.TLabel')
Diamelbl.grid(column=0, row=8, sticky=(W,N,E,S), columnspan=2, pady=(30, 0))
ABlbl1 = Label(second_frame, text='A-B', style='encabezado.TLabel')
ABlbl1.grid(column=0, row=9, sticky=(W,N,E,S))
BClbl1 = Label(second_frame, text='B-C', style='encabezado.TLabel')
BClbl1.grid(column=0, row=10, sticky=(W,N,E,S))
CDlbl1 = Label(second_frame, text='C-D', style='encabezado.TLabel')
CDlbl1.grid(column=0, row=11, sticky=(W,N,E,S))
DAlbl1 = Label(second_frame, text='D-A', style='encabezado.TLabel')
DAlbl1.grid(column=0, row=12, sticky=(W,N,E,S))
AB_lbl = Entry(second_frame,width='8')
AB_lbl.grid(column=1, row=9)
BC_lbl = Entry(second_frame,width='8')
BC_lbl.grid(column=1, row=10)
CD_lbl = Entry(second_frame,width='8')
CD_lbl.grid(column=1, row=11)
DA_lbl = Entry(second_frame,width='8')
DA_lbl.grid(column=1, row=12)

# TRAMO 2
tramo2lbl = Label(second_frame, text='2 Tramo', style='encabezado.TLabel')
tramo2lbl.grid(column=5, row=2, columnspan=4)

longlbl2 = Label(second_frame, text='Longitud', style='encabezado.TLabel')
longlbl2.grid(column=5, row=3, sticky=(W,N,E,S))
mlbl2 = Label(second_frame, text='m', style='encabezado.TLabel')
mlbl2.grid(column=6, row=3, sticky=(W,N,E,S))
kmlbl2 = Label(second_frame, text='Km', style='encabezado.TLabel')
kmlbl2.grid(column=7, row=3, sticky=(W,N,E,S))
materiallbl2 = Label(second_frame, text='Material', style='encabezado.TLabel')
materiallbl2.grid(column=8, row=3, sticky=(W,N,E,S))
ADlbl2 = Label(second_frame, text='A-D', style='encabezado.TLabel')
ADlbl2.grid(column=5, row=4, sticky=(W,N,E,S))
DElbl2 = Label(second_frame, text='D-E', style='encabezado.TLabel')
DElbl2.grid(column=5, row=5, sticky=(W,N,E,S))
EFlbl2 = Label(second_frame, text='E-F', style='encabezado.TLabel')
EFlbl2.grid(column=5, row=6, sticky=(W,N,E,S))
FAlbl2 = Label(second_frame, text='F-A', style='encabezado.TLabel')
FAlbl2.grid(column=5, row=7, sticky=(W,N,E,S))

AD_lbl = Entry(second_frame,width='8')
AD_lbl.grid(column=6, row=4)
DE_lbl = Entry(second_frame,width='8')
DE_lbl.grid(column=6, row=5)
EF_lbl = Entry(second_frame,width='8')
EF_lbl.grid(column=6, row=6)
FA_lbl = Entry(second_frame,width='8')
FA_lbl.grid(column=6, row=7)

material_AD_lbl = Entry(second_frame,width='8')
material_AD_lbl.grid(column=8, row=4)
material_DE_lbl = Entry(second_frame,width='8')
material_DE_lbl.grid(column=8, row=5)
material_EF_lbl = Entry(second_frame,width='8')
material_EF_lbl.grid(column=8, row=6)
material_FA_lbl = Entry(second_frame,width='8')
material_FA_lbl.grid(column=8, row=7)

Diamelbl = Label(second_frame, text='Diámetro', style='encabezado.TLabel')
Diamelbl.grid(column=5, row=8, sticky=(W,N,E,S), columnspan=2, pady=(30, 0))
ADlbl2 = Label(second_frame, text='A-D', style='encabezado.TLabel')
ADlbl2.grid(column=5, row=9, sticky=(W,N,E,S))
DElbl2 = Label(second_frame, text='D-E', style='encabezado.TLabel')
DElbl2.grid(column=5, row=10, sticky=(W,N,E,S))
EFlbl2 = Label(second_frame, text='E-F', style='encabezado.TLabel')
EFlbl2.grid(column=5, row=11, sticky=(W,N,E,S))
FAlbl2 = Label(second_frame, text='F-A', style='encabezado.TLabel')
FAlbl2.grid(column=5, row=12, sticky=(W,N,E,S))
AD_lbl = Entry(second_frame,width='8')
AD_lbl.grid(column=6, row=9)
DE_lbl = Entry(second_frame,width='8')
DE_lbl.grid(column=6, row=10)
EF_lbl = Entry(second_frame,width='8')
EF_lbl.grid(column=6, row=11)
FA_lbl = Entry(second_frame,width='8')
FA_lbl.grid(column=6, row=12)

# CALCULAR

root.mainloop()