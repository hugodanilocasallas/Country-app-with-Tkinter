from tkinter import *
class Window():
    def __init__(self):
        self.root = Tk()
        self.lbl_1=Label(self.root,text="Seleccione su pais",bg="white",fg="black",width="0",font=("Centaur",30),borderwidth=1, relief="solid")
        self.root.geometry("400x250")
        self.Drop_c = StringVar()
        self.options=[]
        self.root.configure(background='white')
        self.root.title('Contry app')
        self.btn_Graficar=Button(self.root,text="Graficar",bg="black",fg="white",width="10", font=("Arial",20),border="1")
    def show(self):
        self.lbl_1.place(x=50, y=50)
        self.btn_Graficar.place(x=50,y=150)
        self.drop = OptionMenu( self.root , self.Drop_c , *self.options )
        self.drop.pack()
        self.drop.place(x=250,y=160)
        self.root.mainloop()

    def getSelected_text(self):        
        return self.Drop_c.get()
    def setOptions(self,options):
        self.options=options


            
