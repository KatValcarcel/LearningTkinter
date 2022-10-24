import tkinter as tk
from tkinter import * #Se importa la librería de Tkinter para la interfaz
from tkinter import messagebox #Se importa messagebox para los mensajes
from math import sqrt

def espacio(a,b,c):

    try:
        global l2,l3,l4,l5
        l2.destroy()
        l3.destroy()
        l4.destroy()
        l5.destroy()
        a = float(a)
        b = float(b)
        c = float(c)
        l2 = Label(root,text=f'\u007B -{b} ± \u221A[(-{b})² - 4×{a}×{c}] \u007D ÷ \u007B2×{a}\u007D',fg='#000',bg='#DDD',font=('Helvetica', 15, 'bold'))
        l2.place(x=185,y=115)
        canvasr = Canvas(root,width=500,height=150)
        canvasr.place(x=100,y=150)
        canvasr.create_line(143,60, 163,80, width=5)
        canvasr.create_line(163,82, 163,30, width=5)
        canvasr.create_line(161,30, 450,30, width=5)
        if comp(a,b,c):
            l3 = Label(root,text=f'-({b}) ±',fg='#000',font=('Helvetica', 25, 'bold'))
            l3.place(x=110,y=190)
            l3 = Label(root,text=f'({b})²',fg='#000',font=('Helvetica', 25, 'bold'))
            l3.place(x=270,y=190)
            l3 = Label(root,text=f'- 4×{a}×{c}',fg='#000',font=('Helvetica', 25, 'bold'))
            l3.place(x=350,y=190)
            canvasr.create_line(20,100, 450,100, width=5)
            l3 = Label(root,text=f'2×{a}',fg='#000',font=('Helvetica', 25, 'bold'))
            l3.place(x=270,y=255)
            x1 = (-1*b + sqrt((b*b) -4*a*c))/(2*a)
            x2 = (-1*b - sqrt((b*b) -4*a*c))/(2*a)
            l4 = Label(root,text=f'X1 = {x1}',bg='#DDD',fg='#000',font=('Helvetica', 25, 'bold'))
            l4.place(x=100,y=335)
            l5 = Label(root,text=f'X2 = {x2}',bg='#DDD',fg='#000',font=('Helvetica', 25, 'bold'))
            l5.place(x=100,y=385)
        else:
            messagebox.showwarning(message="¡Entrada Compleja!\nLa solución estará dada por números complejos.",title="Precaución")
            l3 = Label(root,text=f'-({b}) ±',fg='#000',font=('Helvetica', 25, 'bold'))
            l3.place(x=110,y=190)
            l3 = Label(root,text=f'({b})²',fg='#F00',font=('Helvetica', 25, 'bold'))
            l3.place(x=270,y=190)
            l3 = Label(root,text=f'- 4×{a}×{c}',fg='#F00',font=('Helvetica', 25, 'bold'))
            l3.place(x=350,y=190)
            canvasr.create_line(20,100, 450,100, width=5)
            l3 = Label(root,text=f'2×{a}',fg='#000',font=('Helvetica', 25, 'bold'))
            l3.place(x=270,y=255)
            x1 = (-1*b/(2*a))
            x1i = sqrt(abs((b*b) -4*a*c))/(2*a)
            x2 = (-1*b)/(2*a)
            x2i = sqrt(abs((b*b) -4*a*c))/(2*a)
            l4 = Label(root,text=f'X1 = {round(x1,4)} + {round(x1i,4)}i',bg='#DDD',fg='#000',font=('Helvetica', 25, 'bold'))
            l4.place(x=100,y=335)
            l5 = Label(root,text=f'X2 = {round(x2,4)} - {round(x2i,4)}i',bg='#DDD',fg='#000',font=('Helvetica', 25, 'bold'))
            l5.place(x=100,y=385)

    except:
        messagebox.showerror(message="¡Error De Entrada!\nIngrese un número válido.",title="Error")

def comp(a,b,c):
    return (-4*a*c) > abs(b*b)

root = Tk()
root.title('Fórmula General')
#root.iconbitmap('resist.ico')
root.configure(background='#DDD') 
root.geometry('750x500')
l2 = Label(root)
l3 = Label(root)
l4 = Label(root)
l5 = Label(root)
# l = Label(root,text='Ernesto Romero',fg='#000',bg='#DDD',font=('Helvetica', 10, 'bold'))
# l.place(x=25,y=5)
l = Label(root,text='Escribe los valores:',fg='#000',bg='#DDD',font=('Helvetica', 12, 'bold'))
l.place(x=25,y=25)
l1 = Label(root,text='ax²:',fg='#000',bg='#DDD',font=('Helvetica', 12, 'bold'))
l1.place(x=195,y=25)
a = StringVar()
a1 = Entry(textvar=a)
a1.place(x=230,y=25,width=50,height=27)
l1 = Label(root,text='bx:',fg='#000',bg='#DDD',font=('Helvetica', 12, 'bold'))
l1.place(x=285,y=25)
b = StringVar()
b1 = Entry(textvar=b)
b1.place(x=315,y=25,width=50,height=27)
l1 = Label(root,text='c:',fg='#000',bg='#DDD',font=('Helvetica', 12, 'bold'))
l1.place(x=375,y=25)
c = StringVar()
c1 = Entry(textvar=c)
c1.place(x=395,y=25,width=50,height=27)
l1 = Label(root,text='\u007B -b ± \u221A[(-b)² - 4ac] \u007D ÷ \u007B2a\u007D',fg='#000',bg='#DDD',font=('Helvetica', 14, 'bold'))
l1.place(x=245,y=70)
btn = Button(root,text='Calcular',fg='#000',bg='#439C0C',font=('Helvetica', 12, 'bold'),command=lambda: espacio(a1.get(),b1.get(),c1.get()))
btn.place(x=500,y=25)

root.mainloop()