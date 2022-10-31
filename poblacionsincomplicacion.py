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
# export: auto-py-to-exe
root=Tk()
root.title('Población futura')
# root.iconbitmap('C:/Users/katherine/Documents/LearningTkinter/EXE/usmp.ico')
root.geometry('700x450+450+150')

anios=[]
poblaciones=[]
refAnio=[]
refPoblacion=[]
refLbls=[]


def abrirMetodos():
    anioStr = list(map(str, anios))

    pobArit = poblaciones
    del pobArit[-1]
    pobArit.append(int(Pf_ma))
    print(f'Población Arit: {pobArit}')

    pobInte = poblaciones
    del pobInte[-1]
    pobInte.append(int(Pf_ma))
    print(f'Población Interés: {pobInte}')

    pobGeo = poblaciones
    del pobGeo[-1]
    pobGeo.append(int(Pf_ma))
    print(f'Población Geométrico: {pobGeo}')

    # GRAFICA 
    x = np.arange(len(anioStr))  # the label locations
    width = 0.20  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width, pobArit, width, label='Mét. Aritmético')
    rects2 = ax.bar(x, pobInte, width, label='Mét. Int. Simple.')
    rects3 = ax.bar(x + width, pobGeo, width, label='Mét. Geográfico.')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Población')
    ax.set_title(f'Población en {e_tiempo.get()} años según los métodos.')
    ax.set_xticks(x, anioStr)
    ax.legend()

    #TODO: arreglar los labels de las barras
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.show()


def AbrirGrafica():

    anioStr = list(map(str, anios))
    plt.rcdefaults()

    fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
    axs[0].bar(anioStr, poblaciones)
    axs[1].scatter(anioStr, poblaciones)
    axs[2].plot(anioStr, poblaciones)
    fig.suptitle(f'Población en {e_tiempo.get()} años')
    plt.show()
    # abrirMetodos()


def CalcularQp():
    dotacion=int(eDot.get())
    ldotacion = Label(root, text=f'Qp = {round((((Pf_mi+Pf_mg)/2)*dotacion)/86400,2)} l/s', font='Arial 17 bold')
    ldotacion.place(x=415, y=330)
    refLbls.append(ldotacion)

def aritmetico():
    rvalores=[]
    tiempo=int(e_tiempo.get())
    for i in range(len(anios)-1):
        r=(float(poblaciones[i+1]) - float(poblaciones[i]))/(float(anios[i+1]) - float(anios[i]))
        rRound=format(round(r, 3))
        rvalores.append(float(rRound))
    
    rp=round(sum(rvalores)/len(rvalores), 3)

    # Pf
    global Pf_ma
    Pf_ma=round(poblaciones[-1]+rp*tiempo,3)
    print(f'Método Aritmético: {Pf_ma}')
    return Pf_ma

def interes():
    rvalores=[]
    tiempo=int(e_tiempo.get())

    for i in range(len(anios)-1):
        r=(poblaciones[i+1] - poblaciones[i])/(poblaciones[i]*((anios[i+1]) - anios[i]))
        rRound=format(round(r, 3))
        rvalores.append(float(rRound))
    rp=round(sum(rvalores)/len(rvalores), 3)

    # Pf
    global Pf_mi
    Pf_mi=round(poblaciones[-1]*(1+rp*tiempo),3)
    print(f'Método Interés: {Pf_mi}')
    return Pf_mi

def geometrico():
    rvalores=[]
    tiempo=int(e_tiempo.get())

    for i in range(len(anios)-1):
        r=((poblaciones[i+1]/poblaciones[i])**(1/(anios[i+1] - anios[i])))-1
        rRound=round(r, 3)
        rvalores.append(rRound)
    rp=round(sum(rvalores)/len(rvalores), 3)

    # Pf
    global Pf_mg
    Pf_mg=round(poblaciones[-1]*((1+rp)**tiempo),3)
    print(f'Método Geométrico: {Pf_mg}')
    return Pf_mg

def graficar():
    # debería ser int Habitantes...
    try:
        ma = aritmetico()
        mi = interes()
        mg = geometrico()
        global Pf
        Pf = ceil((mi+mg)/2)
        anios.append(anios[-1]+int(e_tiempo.get()))
        poblaciones.append(Pf)

        print(f'Anio: {anios}')
        print(f'Poblacion: {poblaciones}')
        

        Lbl1 = Label(root, text=f'Método Aritmético:', font='Arial 10')
        Lbl1.place(x=310, y=130)
        lma = Label(root, text=f'Pf= {int(ma)} habitantes', font='Arial 10 bold')
        lma.place(x=500, y=130)
        Lbl1 = Label(root, text=f'Método Interés Simple:', font='Arial 10')
        Lbl1.place(x=310, y=160)
        lmi = Label(root, text=f'Pf= {int(mi)} habitantes', font='Arial 10 bold')
        lmi.place(x=500, y=160)
        Lbl1 = Label(root, text='Método Geométrico: ', font='Arial 10')
        Lbl1.place(x=310, y=190)
        lmg = Label(root, text=f'Pf= {int(mg)} habitantes', font='Arial 10 bold')
        lmg.place(x=500, y=190)

        lPf = Label(root, text=f'Pf= {Pf} habitantes', font='Arial 13 bold')
        lPf.place(x=310, y=220)
        btnGrafica = Button(root, text="Abrir Gráfica", width=20, command=AbrirGrafica)
        btnGrafica.place(x=500, y=220)

        lDot = Label(root, text=f'Dotación', font='Arial 13')
        lDot.place(x=310, y=280)
        global eDot
        eDot = Entry(root, width=10)
        eDot.place(x=400, y=280)
        bDot = Button(root, text="Calcular Qp", width=15, command=CalcularQp)
        bDot.place(x=520, y=280)

        refLbls.append(btnGrafica)
        refLbls.append(lma)
        refLbls.append(lmi)
        refLbls.append(lmg)
        refLbls.append(lPf)
        refLbls.append(lDot)


    except NameError as e:
        messagebox.showerror(message=e,title="Error")

def guardarData():
    anios.clear()
    poblaciones.clear()

    for x in refAnio:
        anios.append(int(x.get()))
    
    for y in refPoblacion:
        poblaciones.append(int(y.get()))

    graficar()

def EnterNumData():
    numData = int(e_data.get())
    if(e_tiempo.get()==''):
        messagebox.showinfo(title='Tiempo', message='Recuerda colocar un periodo antes de presionar el botón calcular')
    label_anio = Label(root, text='Año', font='Arial 13')
    label_anio.place(x=30, y=100)
    label_poblacion = Label(root, text='Población',font='Arial 13')
    label_poblacion.place(x=145, y=100)
    ejey=130

    
    if(len(refPoblacion)!=0):
        for ref in refAnio:
            ref.destroy()
        for refP in refPoblacion:
            refP.destroy()    
        for refL in refLbls:
            refL.destroy() 
        refLbls.clear()    
        refPoblacion.clear()
        refAnio.clear()

    for j in range(numData):
        e_anio=Entry(root, width=10)
        e_anio.place(x=20, y=ejey+30*j+1)
        e_poblacion=Entry(root, width=10)
        e_poblacion.place(x=150, y=ejey+30*j+1)
        refAnio.append(e_anio)
        refPoblacion.append(e_poblacion)
        if(j+1==numData):
            btnCalcular = Button(root, text="Calcular", width=10, command=guardarData)
            btnCalcular.place(x=80, y=ejey+(30*numData))
            refLbls.append(btnCalcular)
            

l_datos = Label(root, text='¿Cuántos datos tiene?')
l_datos.place(x=150,y=25)
e_data=Entry(root, width=20)
e_data.place(x=300, y=25)
botonGenerar = Button(root, text="Generar Espacios", command=EnterNumData)
botonGenerar.place(x=450, y=25)

l_tiempo = Label(root, text='Tiempo')
l_tiempo.place(x=150, y=50)
l_tiempo2 = Label(root, text='años')
l_tiempo2.place(x=370, y=55)
e_tiempo=Entry(root, width=10)
e_tiempo.place(x=300, y=50)




root.mainloop()