from PackDATA.ZoneTouristique import ZoneTouristique 
class MonumentHistorique(ZoneTouristique):
    Mon=['Tour Hassan','Oudaya','Chellah']
    MonII=['Ein Zarqa','Qasr Khalifi']
    mon=''
    zone=''
    def __init__(self,zone,mon='Catrgorie Monument Historique'):
        ZoneTouristique.__init__(self,zone)
        self.mon=mon
    def MCategoryI(self): 
        print('La categorie choisie est -----Monument Historique-----\n')
        print('\t****** Les Sites de Categorie Monument Histrique sont: *****\n')
        print('\t',self.Mon[0],' \n \t', self.Mon[1], '\n \t', self.Mon[2], '\n')
        return(True)
    def MThemeHistoryI(self): 
        print('Le theme choisie est -----Histoire-----\n')
        print('\t****** Les Sites de Theme Histoire sont: *****\n')
        print('\t',self.Mon[0],'\n \t',self.Mon[1] ,'\n \t',self. Mon[2],'\n')
        return(True)
    def MCategoryII(self): 
        print('La categorie choisie est -----Monument Historique-----\n')
        print('\t****** Les Sites de Categorie Monument Histrique sont: *****\n')
        print('\t', self.MonII[0], '\n \t', self.MonII[1], '\n ')
        return(True)
    def MThemeHistoryII(self): 
        print('Le theme choisie est -----Histoire-----\n')
        print('\t****** Les Sites de Theme Histoire sont: *****\n')
        print('\t', self.MonII[0] ,'\n \t' ,self.MonII[1], '\n')
        return(True)
    


        
        
        
        
        

