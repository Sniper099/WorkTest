from PackDATA.ZoneTouristique import ZoneTouristique 
class Musee(ZoneTouristique):
    Mus=['Le Musee Mohammed VI','Musee Belghazi','Musee Maroc Télécom']
    mus=''
    zone=''
    def __init__(self,zone,mus='Categorie Musée'):
        ZoneTouristique.__init__(self,zone)
        self.mus=mus
    def MuCategoryI(self): 
        print('La categorie choisie est -----Musée-----\n')
        print('\t****** Les Sites de Categorie Musée sont: *****\n')
        print('\t', self.Mus[0], '\n \t' ,self.Mus[1],'\n \t' ,self.Mus[2], '\n')
        return(True)
    def MThemeArtI(self): 
        print('Le theme choisie est -----Art moderne-----\n')
        print('\t****** Le/Les Sites de Theme Art moderne est/sont: *****\n')
        print('\t',self.Mus[0], '\n')
        return(True)
    def MThemeEthnoI(self): 
        print('Le theme choisie est -----Ethnographie-----\n')
        print('\t****** Le/Les Sites de Theme Ethnographie est/sont: *****\n')
        print('\t' ,self.Mus[1], '\n')
        return(True)
    def MThemeTelecomI(self): 
        print('Le theme choisie est -----Telécommunications-----\n')
        print('\t****** Le/Les Sites de Theme Telecommunications est/sont: *****\n')
        print('\t' ,self.Mus[2],'\n')
        return(True)
    

    
        
        
        
        