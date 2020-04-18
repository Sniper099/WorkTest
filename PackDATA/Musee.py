import ZoneTouristique
class Musee(ZoneTouristique):
    Mus=['Le Musée Mohammed VI','Musée Belghazi','Musée Maroc Télécom']
    mus=''
    zone=''
    def __init__(self,zone):
        ZoneTouristique.__init__(self,zone)
        self.mus='Catégorie Musée'
    def MuCategoryI(self): 
        print('La catégorie choisie est -----Musée-----\n')
        print('\t****** Les Sites de Catégorie Musée sont: *****\n')
        print('\t', self.Mus[0], '\n \t' ,self.Mus[1],'\n \t' ,self.Mus[2], '\n')
        return(True)
    def MThemeArtI(self): 
        print('Le thème choisie est -----Art moderne-----\n')
        print('\t****** Le/Les Sites de Thème Art moderne est/sont: *****\n')
        print('\t',self.Mon[0], '\n')
        return(True)
    def MThemeEthnoI(self): 
        print('Le thème choisie est -----Ethnographie-----\n')
        print('\t****** Le/Les Sites de Thème Ethnographie est/sont: *****\n')
        print('\t' ,self.Mon[1], '\n')
        return(True)
    def MThemeTelecomI(self): 
        print('Le thème choisie est -----Télécommunications-----\n')
        print('\t****** Le/Les Sites de Thème Télécommunications est/sont: *****\n')
        print('\t' ,self.Mon[2],'\n')
        return(True)

    
        
        
        
        