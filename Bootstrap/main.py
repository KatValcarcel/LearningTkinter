import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
root.title('Ttk Bootstrap') 
# root = ttk.Window(themename="darkly")

b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY)
b1.pack(side=LEFT, padx=5, pady=5)

bo = ttk.Button(root, text='primary', bootstyle='outline')
bo.pack(side=LEFT, padx=5, pady=5)

b2 = ttk.Button(root, text='secondary', bootstyle=SECONDARY)
b2.pack(side=LEFT, padx=5, pady=5)

chk = ttk.Checkbutton(root, text='checkbutton', bootstyle='SUCCESS')
chk.pack(side=LEFT, padx=5, pady=5)

chk2 = ttk.Checkbutton(root, text='round-toggle', bootstyle='round-toggle')
chk2.pack(side=LEFT, padx=5, pady=5)

chk3 = ttk.Checkbutton(root, text='square-toggle', bootstyle='success-square-toggle')
chk3.pack(side=LEFT, padx=5, pady=5)

combo = ttk.Combobox(root, text='Combo', bootstyle='danger')
combo.pack(side=LEFT, padx=5, pady=5)

combo['values'] = (' India',  
                          ' China', 
                          ' Australia', 
                          ' Nigeria', 
                          ' Malaysia', 
                          ' Italy', 
                          ' Turkey', 
                          ' Canada') 

# combo event 
def callback():
    l2.configure(text=cmb.get())

course=["Pizza","Burger","Noodles"]

l1=ttk.Label(root,text="Choose Your Favorite Food")
l1.pack(side=LEFT, padx=5, pady=5)
cmb=ttk.Combobox(root,values=course,width=30)
cmb.pack(side=LEFT, padx=5, pady=5)
cmb.current(0)

btn=ttk.Button(root,text="Click Here",command=callback)
btn.pack(side=LEFT, padx=5, pady=5)

l2=ttk.Label(root,text="")
l2.place(x=900,y=30)

root.mainloop()
