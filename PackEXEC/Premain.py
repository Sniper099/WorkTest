from PackDATA import *
def UserIntercat():
    AffZone()
    print('*********Veuillez choisie une Zone Touristique S Il VOUS PLAIT********')
    zon=string(input('Veuillez entrer le nom de La Zone Touristique'))   
    SelectZone(zon)
    print('----------La Zone Touristique choisie est La Zone de :', zon, '\n')
    print('Pour lister toutes les site de la Zone Touristique ',zon,'Cliquez sur: \t 1 \n')
    print('Pour lister les sites de La Zone Touristique ',zon,'Selon Categorie Cliquez sur: \t 2 \n')
    print('Pour lister les sites de La Zone Touristique ',zon,'Selon Theme Cliquez sur: \t 3 \n')
    print('Pour lister les sites de La Zone Touristique ',zon,'qui proposent une Visite Guidée Cliquez sur: \t 4 \n')
    Number=int(input('Entrer le nom de Service désiré'))
    #Selon les Numbers on aura des actions
    

    
