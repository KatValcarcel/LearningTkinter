import tkinter 
from tkinter import *
from tkinter.tix import COLUMN

# --inicio--
root=Tk()
root.geometry('400x200')
root.title('Número de datos')
l_datos = Label(root, text='¿Cuántos datos tiene?').pack()
e_data=Entry(root, width=20)
e_data.pack()
l_tiempo = Label(root, text='Ingrese periodo').pack()
e_tiempo=Entry(root, width=20)
e_tiempo.pack()


def EnterNumData():
    numData = e_data.get()
    tiempo = e_tiempo.get()
    ventana = Toplevel()
    ventana.title('Población futura')
    ventana.geometry('900x700+450+150')
    l_tiempo= Label(ventana, text=f'Tiempo: {tiempo}').pack()



Button(root, text="Listo", command=EnterNumData).pack()








root.mainloop()