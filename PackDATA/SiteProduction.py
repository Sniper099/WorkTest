from ZoneTouristique import ZoneTouristique
class SiteProduction(ZoneTouristique):
    Prod=['Village de poterie Oulja','Ancienne MÃ©dina Rabat']
    ProdII=['Quissariat Neqra','Sidi Boulfdayl','Al Aqwass']
    prod=''
    zone=''
    def __init__(self,zone,prod='Catégorie Site de Production'):
        ZoneTouristique.__init__(self,zone)
        self.prod=prod
    def PCategoryI(self): 
        print('La catÃ©gorie choisie est -----Site de Production-----\n')
        print('\t****** Les Sites de Catégorie Site de Production sont: *****\n')
        print('\t', self.Prod[0], '\n \t', self.Prod[1], '\n ')
        return(True)
    def MThemeArtI(self): 
        print('Le thème choisie est -----Artisanat-----\n')
        print('\t****** Les Sites de ThÃ¨me Artisanat sont: *****\n')
        print('\t', self.Prod[0],'\n \t', self.Prod[1], '\n ')
        return(True)
    def PCategoryII(self): 
        print('La catégorie choisie est -----Site de Production-----\n')
        print('\t****** Les Sites de CatÃ©gorie Site de Production sont: *****\n')
        print('\t',self.ProdII[0], '\n \t', self.ProdII[1], '\n \t', self.ProdII[2],'\n ')
        return(True)
    def MThemeArtII(self): 
        print('Le thème choisie est -----Artisanat-----\n')
        print('\t****** Les Sites de Thème Artisanat sont: *****\n')
        print('\t' ,self.ProdII[0], '\n \t' ,self.ProdII[1], '\n \t', self.ProdII[2], '\n')
        return(True)
        

        
        