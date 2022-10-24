import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
import math
from turtle import width
from tkinter import messagebox

# --inicio--
root=Tk()
root.title('Población futura')
root.geometry('900x700+450+150')

anio=[]
poblacion=[]
refAnio=[]
refPoblacion=[]

def graficar():
    # try:

        rvalores=[]
        rp=0
        pf=0
        l2 = Label(root, text=f'A ver csm', font='Arial 15')
        l2.place(x=350, y=130)
    # except:
    #     messagebox.showerror(message='¡algo salió mal!',title="Error")

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
    label_anio = Label(root, text='Año', font='Arial 20')
    label_anio.place(x=20, y=100)
    label_poblacion = Label(root, text='Población',font='Arial 20')
    label_poblacion.place(x=150, y=100)
    label_metodo1 = Label(root, text='Método Aritmético', font='Arial 25 bold')
    label_metodo1.place(x=300, y=100)
    btnCalcular = Button(root, text="Calcular todo", width=10, command=guardarData)
    btnCalcular.place(x=700, y=100)
    ejey=130
    for j in range(int(numData)):
        e_anio=Entry(root, width=10)
        e_anio.place(x=20, y=ejey+30*j+1)
        e_poblacion=Entry(root, width=10)
        e_poblacion.place(x=150, y=ejey+30*j+1)
        refAnio.append(e_anio)
        refPoblacion.append(e_poblacion)




l_datos = Label(root, text='¿Cuántos datos tiene?')
l_datos.place(x=150,y=25)
e_data=Entry(root, width=20)
e_data.place(x=300, y=25)
botonGenerar = Button(root, text="Generar", command=EnterNumData)
botonGenerar.place(x=500, y=25)

l_tiempo = Label(root, text='Tiempo')
l_tiempo.place(x=150, y=50)
e_tiempo=Entry(root, width=20)
e_tiempo.place(x=300, y=50)




root.mainloop()