import ProcServe
import Eten
def UserIntercat():
    ProcServe.AffZone()
    print('*********Veuillez choisir une Zone Touristique S Il VOUS PLAIT******** \n')
    zon='' 
    while((zon!='Rabat-Sale')and (zon!='Tiznit')):
        zon=str(input('Veuillez entrer le nom de La Zone Touristique: \t'+'\n'))
        ProcServe.SelectZone(zon)
    Number=0
    while(Number!=6):
        print('Pour lister toutes les site de la Zone Touristique ',zon,'Cliquez sur: \t 1 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'Selon Categorie Cliquez sur: \t 2 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'Selon Theme Cliquez sur: \t 3 \n')
        print('Pour lister les sites de La Zone Touristique ',zon,'qui proposent une Visite Guidée Cliquez sur: \t 4 \n')
        print('Pour effectuer l eteniraire des sites de La Zone Touristique ',zon,'Cliquez sur: \t 5 \n')
        print('Pour quitter le gestionnaire de La Zone Touristique ',zon,'Cliquez sur: \t 6 \n')                
        Number=int(input('Entrer le nombre de Service désiré: \n'))        #Selon les Numbers on aura des actions
        if(Number==1):
            ProcServe.AffSites(zon)
        elif(Number==2):
            ProcServe.Category(zon)
        elif(Number==3):
            ProcServe.Theme(zon)
        elif(Number==4):
            ProcServe.Visite(zon)
        elif(Number==5):
            Eten.Itener(zon)
        else:
            break

    
