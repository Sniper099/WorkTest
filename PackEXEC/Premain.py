import Proc 
from PackETEN.Eten import *
def UserIntercat():
    Proc.AffZone()
    print('*********Veuillez choisir une Zone Touristique S Il VOUS PLAIT********')
    zon=str(input('Veuillez entrer le nom de La Zone Touristique'))   
    Proc.SelectZone(zon)
    Number=0
    while(Number!=5):
        print('----------La Zone Touristique choisie est La Zone de :', zon, '\n')
        print('Pour lister toutes les site de la Zone Touristique ',zon,'Cliquez sur: \t 1 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'Selon Categorie Cliquez sur: \t 2 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'Selon Theme Cliquez sur: \t 3 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'qui proposent une Visite Guidée Cliquez sur: \t 4 \n')
        Number=int(input('Entrer le nom de Service désiré'))        #Selon les Numbers on aura des actions
        if(Number==1):
            Proc.AffSites(zon)
        elif(Number==2):
            Proc.Category(zon)
        elif(Number==3):
            Proc.Theme(zon)
        elif(Number==4):
            Proc.Visite(zon)
        elif(Number==5):
            Itener(zon)
        else:
            break

    
