import numpy as np
import sys
def Itener(zon):
    Nu=int(input('Veuillez entrez le nombre de sites visités ou que vous voulez visiter :\t' ))  #nombre de site parcorrue
    SI=['Tour Hassan','Oudaya','Chellah','Le Musee Mohammed VI','Musee Belghazi','Musee Maroc Telecom','Village de poterie Oulja','Ancienne Medina Rabat','Oued Bouregreg','Jardin exotique']
    dictioI={'Tour Hassan': 0, 'Oudaya': 1, 'Chellah': 2, 'Le Musee Mohammed VI': 3, 'Musee Belghazi': 4, 'Musee Maroc Telecom': 5, 'Village de poterie Oulja': 6, 'Ancienne Medina Rabat': 7, 'Oued Bouregreg': 8, 'Jardin exotique': 9}
    SII=['Ein Zarqa','Mirleft','Quissariat Neqra','Ouad Assaka','Targa','Sidi Boulfdayl','Al Aqwass','Qasr Khalifi']
    dictioII={'Ein Zarqa': 0, 'Mirleft': 1, 'Quissariat Neqra': 2,'Ouad Assaka': 3,'Targa': 4,'Sidi Boulfdayl': 5,'Al Aqwass': 6,'Qasr Khalifi': 7}
    S=[]
    D=0  #La distance
    if zon=='Rabat-Sale':
        print('Veuillez choisir parmis les sites disponibles :')
        for i in SI:
            print('>>>Site Touristique :' + i)
        for i in range(Nu):
            site=str(input('Veuillez preciser le site touristique visité/à visiter : \n'))
            while (site not in dictioI):
                site=str(input('Vous avez mal ecrit le site! Essayer une autre fois SVP! \n'))
            S.append(site)
        matrix= np.loadtxt('Matrix1.txt', usecols=range(10))  #on importe notre matrice a l'aide de numpy pour pouvoire faire des traitements
        for i in range(len(S)-1):
            D+=matrix[dictioI[S[i]]][dictioI[S[i+1]]]
        print("la distance de cet intineraire est: " + str(D) +"km \n")
       
    if zon=='Tiznit':
        print('Veuillez choisir parmis les sites disponibles :')
        for i in SII:
            print('>>>Site Touristique :' + i)
        for i in range(Nu):
            site = str(input('Veuillez preciser le site touristique visité/à visiter : \n'))
            while (site not in dictioII):
                site = str(input('Vous avez mal ecrit le site! Essayer une autre fois SVP! \n'))
            S.append(site)
        matrix= np.loadtxt('Matrix2.txt', usecols=range(8))
        for i in range(len(S)-1):
            D+=matrix[dictioII[S[i]]][dictioII[S[i+1]]]
        print('Vous avez parcorru ou vous allez parcourir est de Distance de : ' + str(D) + 'km \n')
      

