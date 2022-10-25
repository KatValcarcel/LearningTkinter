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

anios=[]
poblaciones=[]
refAnio=[]
refPoblacion=[]

def graficar():
    try:
        rvalores=[]
        rp=0
        pf=0
        # no me juzguen
        l1 = Label(root, text='r =', font='Arial 15 bold')
        l1.place(x=310, y=140)
        l2 = Label(root, text='(Población actual - Población anterior)', font='Arial 15 underline bold')
        l2.place(x=350, y=130)
        l3 = Label(root, text='   (Tiempo actual - Tiempo anterior)', font='Arial 15 bold')
        l3.place(x=350, y=150)

        ejey=170
        # TODO: limpiar cálculo, ref labels
        #TODO: barra lateral en ventana
        for i in range(len(anios)-1):
            print('ejey: ', ejey)
            l1 = Label(root, text=f'r{i+1} = ', font='Arial 15')
            l1.place(x=310, y=ejey+30)
            l2 = Label(root, text=f'{poblaciones[i+1]} - {poblaciones[i]}', font='Arial 15 underline')
            l2.place(x=350, y=ejey+20)
            l3 = Label(root, text=f'{anios[i+1]} - {anios[i]}', font='Arial 15')
            l3.place(x=350, y=ejey+40)
            r=(float(poblaciones[i+1]) - float(poblaciones[i]))/(float(anios[i+1]) - float(anios[i]))
            rRound=format(round(r, 3))
            rlabel=Label(root, text=f'= {rRound}', font='Arial 15')
            rlabel.place(x=450, y=ejey+30)
            rvalores.append(rRound)
            ejey=ejey+50

    except:
        messagebox.showerror(message='Algo salió mal',title="Error")



def guardarData():
    anios.clear()
    poblaciones.clear()
    for x in refAnio:
        anios.append(x.get())
    
    for y in refPoblacion:
        poblaciones.append(y.get())
    print(f'Anio: {anios}')
    print(f'Poblacion: {poblaciones}')

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
    
    if(len(refAnio)!=0):
        for ref in refAnio:
            ref.destroy()
        for refP in refPoblacion:
            refP.destroy()      
        refPoblacion.clear()
        refAnio.clear()

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
# botonLimpiar = Button(root, text="Borrar", command=borrar)
# botonLimpiar.place(x=600, y=25)

l_tiempo = Label(root, text='Tiempo')
l_tiempo.place(x=150, y=50)
e_tiempo=Entry(root, width=20)
e_tiempo.place(x=300, y=50)




root.mainloop()