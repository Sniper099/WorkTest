from PackDATA.ZoneTouristique import ZoneTouristique 
class SiteProduction(ZoneTouristique):
    Prod=['Village de poterie Oulja','Ancienne Medina Rabat']
    ProdII=['Quissariat Neqra','Sidi Boulfdayl','Al Aqwass']
    prod=''
    zone=''
    def __init__(self,zone,prod='Categorie Site de Production'):
        ZoneTouristique.__init__(self,zone)
        self.prod=prod
    def PCategoryI(self): 
        print('La categorie-----Site de Production-----\n')
        print('\t****** Les Sites de Categorie Site de Production sont: *****\n')
        print('\t >', self.Prod[0], '\n \t >', self.Prod[1], '\n ')
        return(True)
    def MThemeArtI(self): 
        print('Le theme-----Artisanat-----\n')
        print('\t****** Les Sites de Theme Artisanat sont: *****\n')
        print('\t >', self.Prod[0],'\n \t >', self.Prod[1], '\n ')
        return(True)
    def PCategoryII(self): 
        print('La categorie-----Site de Production-----\n')
        print('\t****** Les Sites de Categorie Site de Production sont: *****\n')
        print('\t >',self.ProdII[0], '\n \t >', self.ProdII[1], '\n \t >', self.ProdII[2],'\n ')
        return(True)
    def MThemeArtII(self): 
        print('Le theme-----Artisanat-----\n')
        print('\t****** Les Sites de Theme Artisanat sont: *****\n')
        print('\t >' ,self.ProdII[0], '\n \t >' ,self.ProdII[1], '\n \t >', self.ProdII[2], '\n')
        return(True)
        

        
        