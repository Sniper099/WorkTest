import numpy as np
import sys
from PackEXEC import *
def intin():
    print("Veuillez preciser le nombre de sites a visiter : ")
    Nu=int(input())  #nombre de site parcorrue
    SI=['Tour Hassan','Oudaya','Chellah','Le Muse Mohammed VI','Muse Belghazi','Muse Maroc Tlcom','Village de poterie Oulja','Ancienne Medina Rabat','Oued Bouregreg','Jardin exotique']
    dictioI={'Tour Hassan': 0, 'Oudaya': 1, 'Chellah': 2, 'Le Muse Mohammed VI': 3, 'Muse Belghazi': 4, 'Muse Maroc Tlcom': 5, 'Village de poterie Oulja': 6, 'Ancienne Medina Rabat': 7, 'Oued Bouregreg': 8, 'Jardin exotique': 9}
    SII=['Ein Zarqa','Mirleft','Quissariat Neqra','Ouad Assaka','Targa','Sidi Boulfdayl','Al Aqwass','Qasr Khalifi']
    dictioII={'Ein Zarqa': 0, 'Mirleft': 1, 'Quissariat Neqra': 2,'Ouad Assaka': 3,'Targa': 4,'Sidi Boulfdayl': 5,'Al Aqwass': 6,'Qasr Khalifi': 7}
    S=[]
    D=0  #La distance
    if zon=='Rabat-Salé':
        print("Voici la liste des sites disponibles :")
        for i in SI:
            print("----site :" + i)
        for i in range(Nu):
            print("Veuillez preciser le nom du site touristique à visiter :")
            site=str(input())
            while (site not in dictioI):
                print("Oups mauvais choix!! entrer une autre zone ^^")
                site=str(input())
            S.append(site)
        matrix= np.loadtxt('Matrix1.txt', usecols=range(10))  #on importe notre matrice a l'aide de numpy pour pouvoire faire des traitements
        for i in range(len(S)-1):
            D+=matrix[dictioI[S[i]]][dictioI[S[i+1]]]
        print("la distance de cet intineraire est: " + str(D) +"km")
       
    if zon=='Tiznit':
        print("Voici la liste des sites disponibles :")
        for i in SII:
            print("----site :" + i)
        for i in range(Nu):
            print("Veuillez preciser le nom du site touristique à visiter :")
            site = str(input())
            while (site not in dictioII):
                print("Oups mauvais choix!! entrer une autre zone ^^")
                site = str(input())
            S.append(site)
        matrix= np.loadtxt('Matrix2.txt', usecols=range(8))
        for i in range(len(S)-1):
            D+=matrix[dictioII[S[i]]][dictioII[S[i+1]]]
        print("la distance de cet intineraire est: " + str(D) +"km")
      

