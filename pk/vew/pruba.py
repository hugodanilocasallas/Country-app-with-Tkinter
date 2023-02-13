# Import module
from tkinter import *
  
#from tkinter import *
import pywhatkit as rep
def aceptar():
    ops = "https://www.youtube.com/watch?v=Pkgd3tER1yI&list=RDMMPkgd3tER1yI&start_radio=1"
    rep.playonyt(ops)

root= Tk() #Almacenar Tk
lbl_1=Label(root,text="¿Mañana no hay clases?",bg="Steelblue",fg="white",width="0",font=("Centaur",30))

lbl_1.place(x=15, y=50)
root.title("Ventana")
root.geometry("380x300")
root.resizable(0,0) #Bloquear tamaño
root.configure(background='Red')

#Numero de filas y columnas
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)
#Boton
btn_si=Button(root,text="Si",bg="Aqua",fg="white",width="5", borderwidth="5",  font=("Arial",20, "bold"),border="1",command=aceptar)
#btn_si.place(x=50,y=150)
btn_si.grid(row=2, column=0) #Colocar el boton dependiendo la fila y columna

btn_no=Button(root,text="No",bg="Aqua",fg="white",width="5", font=("Arial",20, "bold"),border="1",command=root.destroy)
#btn_si.place(x=50,y=150)
btn_no.grid(row=2, column=1) #Colocar el boton dependiendo la fila y columna

def Click():
    cap = campo.get()
    et1= Label(root, text=cap, fg= "Steelblue1", font=("Verdana", 14, "bold"))
    et1.grid(row=4, column=2)

#Button ingreso xd
btn= Button(root, text="Ingreso", command=Click)
btn.grid(row=3, column=2)

#Ingreso de texto (campo)
campo= Entry(root, width=25, bg="White", fg="Blue", borderwidth=5)
campo.grid(row=2, column=2)

for widget in root.grid_slaves():
    if widget.grid_info()['row']==4:
        widget.grid_forget()


root.mainloop()