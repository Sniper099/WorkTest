from PackDATA import *
def UserIntercat():
    AffZone()
    print('*********Veuillez choisir une Zone Touristique S Il VOUS PLAIT********')
    zon=string(input('Veuillez entrer le nom de La Zone Touristique'))   
    SelectZone(zon)
    Number=0
    while(Number!=5):
        print('----------La Zone Touristique choisie est La Zone de :', zon, '\n')
        print('Pour lister toutes les site de la Zone Touristique ',zon,'Cliquez sur: \t 1 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'Selon Categorie Cliquez sur: \t 2 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'Selon Theme Cliquez sur: \t 3 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'qui proposent une Visite Guidée Cliquez sur: \t 4 \n')
        AffZoneNumber=int(input('Entrer le nom de Service désiré'))
        #Selon les Numbers on aura des actions
        if(Number==1):
            AffSites(zon)
        elif(Number==2):
            Category(zon)
        elif(Number==3):
            Theme(zon)
        elif(Number==4):
            Visite(zon)
        else:
            break

    
