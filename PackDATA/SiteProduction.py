import ZoneTouristique
class SiteProduction(ZoneTouristique):
    Prod=['Village de poterie Oulja','Ancienne Médina Rabat']
    ProdII=['Quissariat Neqra','Sidi Boulfdayl','Al Aqwass']
    prod=''
    zone=''
    def __init__(self,zone):
        ZoneTouristique.__init__(self,zone)
        self.prod='Catégorie Site de Production'
    def PCategoryI(self): 
        print('La catégorie choisie est -----Site de Production-----\n')
        print('\t****** Les Sites de Catégorie Site de Production sont: *****\n')
        print('\t', self.Prod[0], '\n \t', self.Prod[1], '\n ')
        return(True)
    def MThemeArtI(self): 
        print('Le th�me choisie est -----Artisanat-----\n')
        print('\t****** Les Sites de Thème Artisanat sont: *****\n')
        print('\t', self.Prod[0],'\n \t', self.Prod[1], '\n ')
        return(True)
    def PCategoryII(self): 
        print('La cat�gorie choisie est -----Site de Production-----\n')
        print('\t****** Les Sites de Catégorie Site de Production sont: *****\n')
        print('\t',self.ProdII[0], '\n \t', self.ProdII[1], '\n \t', self.ProdII[2],'\n ')
        return(True)
    def MThemeArtII(self): 
        print('Le thème choisie est -----Artisanat-----\n')
        print('\t****** Les Sites de Thème Artisanat sont: *****\n')
        print('\t' ,self.ProdII[0], '\n \t' ,self.ProdII[1], '\n \t', self.ProdII[2], '\n')
        return(True)
        
        
        