from ast import main
from textwrap import fill
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
# from tkinter.tix import ButtonBox
from tkinter.ttk import *
from turtle import color, width
from tkinter import messagebox
import math
from math import ceil
from warnings import catch_warnings
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import sys
import os
from PIL import ImageTk, Image
# --inicio--
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# export: auto-py-to-exe

root=Tk()
root.title('Hardy Cross')
iconPath = resource_path('usmp.ico')
root.iconbitmap(iconPath)
root.geometry('1080x450+450+150')
root.state('zoomed')

tramo1_km=[]
tramo2_km=[]
tramo1_diametros=[]
tramo2_diametros=[]
tramo1_materiales=[]
tramo2_materiales=[]
entriesMetro1=[]
entriesMetro2=[]
entriesDiametros1=[]
entriesDiametros2=[]
entriesMateriales1=[]
entriesMateriales2=[]
kmlbl=[]

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

canvasgrafico = Canvas(second_frame, bg='white')
canvasgrafico.grid(column=13,row=0, rowspan=13, columnspan=7, padx=(20,0))
canvasgrafico.create_polygon(105, 150, 135, 80, 255, 80, 285, 150,195,190, outline = 'blue', fill='white') 
canvasgrafico.create_line (195, 190, 195, 80, fill ='blue') 
canvasgrafico.create_line (105, 150, 105, 175, fill ='red') 
canvasgrafico.create_line (135, 80, 110, 60, fill ='red') 
canvasgrafico.create_line (195, 80, 165, 60, fill ='red') 
canvasgrafico.create_line (195, 80, 225, 40, fill ='red') 
canvasgrafico.create_line (255, 80, 285, 60, fill ='red') 
canvasgrafico.create_line (285, 150, 285, 175, fill ='red') 
canvasgrafico.create_line (195, 190, 225, 150, fill ='red') 
canvasgrafico.create_line (195, 190, 225, 215, fill ='red') 

# entradas
e_m9=Entry(canvasgrafico,width='5')
e_m9.place(x=79, y=175)
e_m3=Entry(canvasgrafico,width='5')
e_m3.place(x=85, y=40)
e_o3=Entry(canvasgrafico,width='5')
e_o3.place(x=140, y=40)
e_o5=Entry(canvasgrafico,width='5',foreground='red')
e_o5.place(x=145, y=82)
e_p7=Entry(canvasgrafico,width='5',foreground='red')
e_p7.place(x=152, y=120)
e_q1=Entry(canvasgrafico,width='5')
e_q1.place(x=220, y=20)
e_s3=Entry(canvasgrafico,width='5')
e_s3.place(x=285, y=40)
e_q5=Entry(canvasgrafico,width='5',foreground='red')
e_q5.place(x=205, y=82)
e_s10=Entry(canvasgrafico,width='5')
e_s10.place(x=265, y=175)
e_q8=Entry(canvasgrafico,width='5')
e_q8.place(x=205, y=135)
e_q13=Entry(canvasgrafico,width='5')
e_q13.place(x=225, y=215)


encabezado = Style()
encabezado.configure("encabezado.TLabel", font='arial 10 bold', width='9', anchor='E')

celda=Style()
celda.configure("celda.TLabel", font='arial 10',width='9', anchor='E')
celdaroja=Style()
celdaroja.configure("celdaroja.TLabel", font='arial 10', foreground='red', width='9', anchor='E')

boton =Style()
boton.configure('Boton.TButton', font='arial 10', width='9', background='#003366', foreground='black', refiel='flat')
boton.map('Boton.TButton', background=[("active","#001933")], foreground=[('active','blCK')])



def llenarEntradas():
    for entry in entriesDiametros1:
        entry.insert(0,'4')
    for entry in entriesDiametros2:
        entry.insert(0,'5')
    for entry in entriesMateriales1:
        entry.insert(0,'100')
    for entry in entriesMateriales2:
        entry.insert(0,'200')
    for entry in entriesMetro1:
        entry.insert(0,'355')
    for entry in entriesMetro2:
        entry.insert(0,'864')
    e_m9.insert(0,'12.49')
    e_m3.insert(0,'18.74')
    e_o3.insert(0,'12.49')
    e_o5.insert(0,'2.49')
    e_p7.insert(0,'8.5')
    e_q1.insert(0,'34.7')
    e_s3.insert(0,'37.48')
    e_q5.insert(0,'11.22')
    e_q8.insert(0,'90.22')
    e_s10.insert(0,'18.74')
    e_q13.insert(0,'24.98')


# GRAFICO
def DatosGrafico():
    global m9
    m9=float(e_m9.get())
    global m3
    m3=float(e_m3.get())
    global o3
    o3=float(e_o3.get())
    global o5
    o5=float(e_o5.get())
    global p7
    p7=float(e_p7.get())
    global q1
    q1=float(e_q1.get())
    global s3
    s3=float(e_s3.get())
    global q5
    q5=float(e_q5.get())
    global q8
    q8=float(e_q8.get())
    global s10
    s10=float(e_s10.get())
    global q13
    q13=float(e_q13.get())

    global m6
    m6=round(m3-(o5),2)
    lblm6 = Label(canvasgrafico, text=m6, font='Arial 8', foreground='red', background='white')
    lblm6.place(x=88, y=100)
    global n10
    n10=round(m6+m9,2)
    lbln10 = Label(canvasgrafico, text=n10, font='Arial 8', foreground='red', background='white')
    lbln10.place(x=135, y=170)
    global s6
    s6=round(s3-q5,2)
    lbls6 = Label(canvasgrafico, text=s6, font='Arial 8', foreground='red', background='white')
    lbls6.place(x=280, y=100)
    global r10
    r10=round(s10+s6,2)
    lbls6 = Label(canvasgrafico, text=r10, font='Arial 8', foreground='red', background='white')
    lbls6.place(x=230, y=175)

def GenerarEncabezados(titulos:list, columna:int, fila:int):
    for title in titulos:
        lbl = Label(second_frame, text=title, style='encabezado.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S), pady=(30, 0))
        columna+=1

def GenerarColumnaTramo1(columna:int, fila:int):
    tramos=['A-B', 'B-C', 'C-D', 'D-A']
    for tramo in tramos:
        lbl = Label(second_frame, text=tramo, style='encabezado.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S))
        fila+=1

def GenerarColumnaTramo2(columna:int, fila:int):
    tramos=['A-D', 'D-E', 'E-F', 'F-A']
    for tramo in tramos:
        lbl = Label(second_frame, text=tramo, style='encabezado.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S))
        fila+=1

def LlenarColumna(valores:list,columna:int,fila:int):
    for valor in valores:
        lbl = Label(second_frame, text=valor, style='celda.TLabel')
        lbl.grid(column=columna, row=fila, sticky=(W,N,E,S))
        fila+=1

# TRAMO 1

tramo1lbl = Label(second_frame, text='1 Tramo', style='encabezado.TLabel')
tramo1lbl.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

longlbl1 = Label(second_frame, text='Longitud', style='encabezado.TLabel')
longlbl1.grid(column=0, row=1, sticky=(W,N,E,S))
mlbl1 = Label(second_frame, text='m', style='encabezado.TLabel')
mlbl1.grid(column=1, row=1, sticky=(W,N,E,S))
kmlbl1 = Label(second_frame, text='Km', style='encabezado.TLabel')
kmlbl1.grid(column=2, row=1, sticky=(W,N,E,S))
materiallbl1 = Label(second_frame, text='Material', style='encabezado.TLabel')
materiallbl1.grid(column=3, row=1, sticky=(W,N,E,S))
Diamelbl = Label(second_frame, text='Diámetro', style='encabezado.TLabel')
Diamelbl.grid(column=4, row=1, sticky=(W,N,E,S))
GenerarColumnaTramo1(0,2)

AB_metro = Entry(second_frame,width='8')
AB_metro.grid(column=1, row=2)
entriesMetro1.append(AB_metro)
BC_metro = Entry(second_frame,width='8')
BC_metro.grid(column=1, row=3)
entriesMetro1.append(BC_metro)
CD_metro = Entry(second_frame,width='8')
CD_metro.grid(column=1, row=4)
entriesMetro1.append(CD_metro)
DA_metro = Entry(second_frame,width='8')
DA_metro.grid(column=1, row=5)
entriesMetro1.append(DA_metro)

material_AB = Entry(second_frame,width='8')
material_AB.grid(column=3, row=2)
entriesMateriales1.append(material_AB)
material_BC = Entry(second_frame,width='8')
material_BC.grid(column=3, row=3)
entriesMateriales1.append(material_BC)
material_CD = Entry(second_frame,width='8')
material_CD.grid(column=3, row=4)
entriesMateriales1.append(material_CD)
material_DA = Entry(second_frame,width='8')
material_DA.grid(column=3, row=5)
entriesMateriales1.append(material_DA)

AB_diametro = Entry(second_frame,width='8')
AB_diametro.grid(column=4, row=2)
entriesDiametros1.append(AB_diametro)
BC_diametro = Entry(second_frame,width='8')
BC_diametro.grid(column=4, row=3)
entriesDiametros1.append(BC_diametro)
CD_diametro = Entry(second_frame,width='8')
CD_diametro.grid(column=4, row=4)
entriesDiametros1.append(CD_diametro)
DA_diametro = Entry(second_frame,width='8')
DA_diametro.grid(column=4, row=5)
entriesDiametros1.append(DA_diametro)

# TRAMO 2
tramo2lbl = Label(second_frame, text='2 Tramo', style='encabezado.TLabel')
tramo2lbl.grid(column=6, row=0, columnspan=4)

longlbl2 = Label(second_frame, text='Longitud', style='encabezado.TLabel')
longlbl2.grid(column=6, row=1, sticky=(W,N,E,S))
mlbl2 = Label(second_frame, text='m', style='encabezado.TLabel')
mlbl2.grid(column=7, row=1, sticky=(W,N,E,S))
kmlbl2 = Label(second_frame, text='Km', style='encabezado.TLabel')
kmlbl2.grid(column=8, row=1, sticky=(W,N,E,S))
materiallbl2 = Label(second_frame, text='Material', style='encabezado.TLabel')
materiallbl2.grid(column=9, row=1, sticky=(W,N,E,S))
Diamelbl = Label(second_frame, text='Diámetro', style='encabezado.TLabel')
Diamelbl.grid(column=10, row=1, sticky=(W,N,E,S))
GenerarColumnaTramo2(6,2)


AD_e = Entry(second_frame,width='8')
AD_e.grid(column=7, row=2)
entriesMetro2.append(AD_e)
DE_e = Entry(second_frame,width='8')
DE_e.grid(column=7, row=3)
entriesMetro2.append(DE_e)
EF_e = Entry(second_frame,width='8')
EF_e.grid(column=7, row=4)
entriesMetro2.append(EF_e)
FA_e = Entry(second_frame,width='8')
FA_e.grid(column=7, row=5)
entriesMetro2.append(FA_e)

material_AD = Entry(second_frame,width='8')
material_AD.grid(column=9, row=2)
entriesMateriales2.append(material_AD)
material_DE = Entry(second_frame,width='8')
material_DE.grid(column=9, row=3)
entriesMateriales2.append(material_DE)
material_EF = Entry(second_frame,width='8')
material_EF.grid(column=9, row=4)
entriesMateriales2.append(material_EF)
material_FA = Entry(second_frame,width='8')
material_FA.grid(column=9, row=5)
entriesMateriales2.append(material_FA)


AD_diametro = Entry(second_frame,width='8')
AD_diametro.grid(column=10, row=2)
entriesDiametros2.append(AD_diametro)
DE_diametro = Entry(second_frame,width='8')
DE_diametro.grid(column=10, row=3)
entriesDiametros2.append(DE_diametro)
EF_diametro = Entry(second_frame,width='8')
EF_diametro.grid(column=10, row=4)
entriesDiametros2.append(EF_diametro)
FA_diametro = Entry(second_frame,width='8')
FA_diametro.grid(column=10, row=5)
entriesDiametros2.append(FA_diametro)



def PrimeraTabla():  
    DatosGrafico()
    encabezados=['TRAMO','L-Km','D-pulg','C','K','Q-l/s','hf','hf/Q']
    GenerarEncabezados(encabezados, 0, 11)   
    FAlbl2 = Label(second_frame, text=f'{chr(916)} Q-l/s', style='encabezado.TLabel')
    FAlbl2.grid(column=8, row=11, columnspan=2, sticky=(W,N,E,S), pady=(30, 0))    
    encabezados2=['Q-l/s','hf-m']
    GenerarEncabezados(encabezados2,10,11)
    GenerarColumnaTramo1(0,12)
    GenerarColumnaTramo2(0,17)

    # graficar km, pulgadas, material
    LlenarColumna(tramo1_km,1,12)
    LlenarColumna(tramo1_diametros,2,12)
    LlenarColumna(tramo1_materiales,3,12)
    LlenarColumna(tramo2_km,1,17)
    LlenarColumna(tramo2_diametros,2,17)
    LlenarColumna(tramo2_materiales,3,17)

    kTramo1=[]
    kTramo2=[]
    for i in range(4):
        k=round(((10**7)*tramo1_km[i]/(5.813*(tramo1_materiales[i]**1.852)*(tramo1_diametros[i]**4.87))),5)
        kTramo1.append(k)
        k2=round(((10**7)*tramo2_km[i]/(5.813*(tramo2_materiales[i]**1.852)*(tramo2_diametros[i]**4.87))),5)
        kTramo2.append(k2)
    LlenarColumna(kTramo1,4,12)
    LlenarColumna(kTramo2,4,17)
    
    qls1=[]
    qls1.append(-o5)
    qls1.append(m6)
    qls1.append(n10)
    qls1.append(p7)
    LlenarColumna(qls1,5,12)
    qls2=[]
    qls2.append(-p7)
    qls2.append(-r10)
    qls2.append(-s6)
    qls2.append(q5)
    LlenarColumna(qls2,5,17)
    
    hf=[]
    hf2=[]
    for i in range(4):
        if i==0:
            h=round(-kTramo1[i]*(abs(qls1[i])**1.852),2)
            h2=round(-kTramo2[i]*(abs(qls2[i])**1.852),2)
        elif i==3:
            h=round(kTramo1[i]*(abs(qls1[i])**1.852),2)
            h2=round(kTramo2[i]*(abs(qls2[i])**1.852),2)
        else:
            h=round(kTramo1[i]*(abs(qls1[i])**1.852),2)
            h2=round(-kTramo2[i]*(abs(qls2[i])**1.852),2)
        hf.append(h)
        hf2.append(h2)
    LlenarColumna(hf,6,12)
    LlenarColumna(hf2,6,17)
    lbl = Label(second_frame, text=round(sum(hf),2), style='celdaroja.TLabel', font='arial 11 bold')
    lbl.grid(column=6, row=16, sticky=(W,N,E,S))
    lbl2 = Label(second_frame, text=round(sum(hf2),2), style='celdaroja.TLabel', font='arial 11 bold')
    lbl2.grid(column=6, row=21, sticky=(W,N,E,S))

    hfq=[]
    hfq2=[]
    for i in range(4):
        hfsq=round(hf[i]/qls1[i],2)
        hfq.append(hfsq)
        hfsq2=round(hf2[i]/qls2[i],2)
        hfq2.append(hfsq2)
    LlenarColumna(hfq,7,12)
    LlenarColumna(hfq2,7,17)

    lbl = Label(second_frame, text=round(sum(hfq),2), style='celda.TLabel', font='arial 11 bold')
    lbl.grid(column=7, row=16, sticky=(W,N,E,S))
    lb2 = Label(second_frame, text=round(sum(hfq2),2), style='celda.TLabel', font='arial 11 bold')
    lb2.grid(column=7, row=21, sticky=(W,N,E,S))



def GuardarDiametrosMateriales():
    for entry in entriesDiametros1:
        tramo1_diametros.append(float(entry.get()))
    for entry in entriesDiametros2:
        tramo2_diametros.append(float(entry.get()))
    for entry in entriesMateriales1:
        tramo1_materiales.append(float(entry.get()))
    for entry in entriesMateriales2:
        tramo2_materiales.append(float(entry.get()))

def ToKm():
    if (len(kmlbl)!=0):
        for lbl in kmlbl:
            lbl.destroy()
        kmlbl.clear()
        tramo1_km.clear()
        tramo2_km.clear()
        tramo1_diametros.clear()
        tramo2_diametros.clear()
        tramo1_materiales.clear()
        tramo2_materiales.clear()

    rowinit=2
    for entry in entriesMetro1:
        km=round(float(entry.get())/1000,3)
        tramo1_km.append(km)
        lbl = Label(second_frame, text=km, style='celda.TLabel')
        lbl.grid(column=2, row=rowinit) 
        kmlbl.append(lbl)
        rowinit+=1

    rowinit=2
    for entry in entriesMetro2:
        km=round(float(entry.get())/1000,3)
        tramo2_km.append(km)
        lbl = Label(second_frame, text=km, style='celda.TLabel')
        lbl.grid(column=8, row=rowinit)
        kmlbl.append(lbl) 
        rowinit+=1

    GuardarDiametrosMateriales()
    
    
def Calcular(*args):
    llenarEntradas()
    ToKm()
    PrimeraTabla()

# CALCULAR
btnCalcular = Button(second_frame, text='Calcular', style='Boton.TButton', command=Calcular)
btnCalcular.grid(column=5,row=8, sticky=(W,N,E,S), pady=(20,0))

# keyPress Enter 
root.bind("<Return>", Calcular)

root.mainloop()