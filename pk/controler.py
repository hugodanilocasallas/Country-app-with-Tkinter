from model.reading import Reading
from vew.grafic import *
from vew.window import Window
def show_grafic(vew,bookman,c_data):
    con=vew.getSelected_text()
    bookman.setTerritory(con)
    years,poblation=bookman.selectCountry(c_data)
    barGrafic(years,poblation)
    
    
def start():
    bookman = Reading()
    c_data=bookman.readcsv()
    #print(type(c_data))
    countrys_of_world=bookman.worldTitles()
    #barGrafic(years,poblation)
    vew = Window()
    vew.setOptions(countrys_of_world)
    vew.show()
    vew.btn_Graficar["command"]=show_grafic(vew,bookman,c_data)
    #print(vew.getSelected_text())
if __name__=="__main__":
    start()