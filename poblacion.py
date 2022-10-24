import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
import math
from turtle import width

# --inicio--
root=Tk()
root.geometry('400x200')
root.title('Número de datos')
l_datos = Label(root, text='¿Cuántos datos tiene?').pack()
e_data=Entry(root, width=20)
e_data.pack()

anio=[]
poblacion=[]
refAnio=[]
refPoblacion=[]

def graficar():
    global l2, l3, l4
    l2.destroy()
    l3.destroy()
    l4.destroy()
    rvalores=[]
    rp=0
    pf=0
    l2 = Label(mainframe,text=f'\u007B -{b} ± \u221A[(-{b})² - 4×{a}×{c}] \u007D ÷ \u007B2×{a}\u007D',fg='#000',bg='#DDD',font=('Helvetica', 15, 'bold'))
    l2.place(x=185,y=115)

def guardarData():
    for x in refAnio:
        anio.append(x.get())
    
    for y in refPoblacion:
        poblacion.append(y.get())

    print(f'Anio: {anio}')
    print(f'Poblacion: {poblacion}')

    graficar()

def EnterNumData():
    numData = e_data.get()
    ventana = Toplevel()
    ventana.title('Población futura')
    ventana.geometry('900x700+450+150')

    mainframe = Frame(ventana)
    mainframe.grid(column=0,row=0, sticky=(W,N,E,S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.columnconfigure(1, weight=1)
    mainframe.columnconfigure(2, weight=1)
    mainframe.columnconfigure(3, weight=1)
    mainframe.columnconfigure(4, weight=1)

    mainframe.rowconfigure(0, weight=1)
    label_anio = Label(mainframe, text='Año', font='Arial 20')
    label_anio.grid(column=0,row=0, sticky=(W,N,E,S))
    label_poblacion = Label(mainframe, text='Población',font='Arial 20')
    label_poblacion.grid(column=1,row=0, sticky=(W,N,E,S))
    label_metodo1 = Label(mainframe, text='Método Aritmético', font='Arial 25 bold')
    label_metodo1.grid(column=2,row=1, columnspan=2, sticky=(W,N,E,S))
    label_tiempo = Label(mainframe, text='Tiempo', font='Arial 20')
    label_tiempo.grid(column=2,row=0, sticky=(W,N,E,S))
    e_tiempo=Entry(mainframe, width=20)
    e_tiempo.grid(column=3, row=0)
    btnCalcular = Button(mainframe, text="Calcular", width=20, command=guardarData)
    btnCalcular.grid(column=4, row=0, sticky=(W,N,E,S))

    for j in range(int(numData)):
        mainframe.rowconfigure(j,weight=1)
        e_anio=Entry(mainframe, width=20)
        e_anio.grid(column=0, row=j+1)
        e_poblacion=Entry(mainframe, width=20)
        e_poblacion.grid(column=1, row=j+1)
        refAnio.append(e_anio)
        refPoblacion.append(e_poblacion)

    for child in mainframe.winfo_children():
        child.grid_configure(ipady=10, padx=1, pady=1)




Button(root, text="Listo", command=EnterNumData).pack()








root.mainloop()