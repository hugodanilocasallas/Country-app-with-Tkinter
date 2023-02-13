import csv
class Reading():
    def __init__(self):
        self.territory="Colombia"
        self.book='D:/Notas de clase/Platzi/git_hub/Country_app/pk/model/Country.csv'
    def setTerritory(self,Territory):
        self.territory=Territory
    
    def readcsv(self):
        with open(self.book, 'r') as csvfile:
            reader= csv.reader(csvfile, delimiter=',')
            header= next(reader)
            #print(header)
            self.data=[]
            for row in reader:  
                iterable= zip (header,row)
                #print("***" * 5)
                #print(list(iterable))
                country_dicc={key: value for key , value in iterable}
            # print(country_dicc)
                self.data.append(country_dicc)
            return self.data

    def selectCountry(self,data):
        #generate_bar_chart()
        #print(data[0])
        self.poblation=[]
        self.titles=[]
        Country=list(filter(lambda item: item['Country/Territory']==self.territory, data))
        country2=Country[0]
        for i in range (1970,2030,10):
            var1='{:,.0f}'.format(int(country2[str(i)+' Population']))
            self.titles.append(str(i))
            self.poblation.append(var1)
        #print(self.titles,self.poblation)
        return self.titles,self.poblation
    def worldTitles(self):
        self.worldList=[]
        contryslist=list(contry['Country/Territory'] for contry in self.data)
        return contryslist
if(__name__=='__main__'): 
    print("in test")

