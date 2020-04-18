import ZoneTouristique
class SiteNatRemrq(ZoneTouristique):
    Nat=['Village de poterie Oulja','Ancienne Médina Rabat']
    NatII=['Mirleft','Ouad Assaka','Targa']
    nat=''
    zone=''
    def __init__(self,zone):
        ZoneTouristique.__init__(self,zone)
        self.nat='Catégorie Site Naturel Remarquable'
    def NCategoryI(self): 
        print('La catégorie choisie est ----- Site Naturel Remarquable-----\n')
        print('\t****** Les Sites de Catégorie Site Naturel Remarquable sont: *****\n')
        print('\t', self.Nat[0], '\n \t' ,self.Nat[1], '\n ')
        return(True)
    def MThemeNatI(self): 
        print('Le thème choisie est -----Nature-----\n')
        print('\t****** Les Sites de Thème Nature sont: *****\n')
        print('\t', self.Nat[0],' \n \t' ,self.Nat[1], '\n ')
        return(True)
    def NCategoryII(self): 
        print('La catégorie choisie est ----- Site Naturel Remarquable-----\n')
        print('\t****** Les Sites de Catégorie Site Naturel Remarquable sont: *****\n')
        print('\t', self.NatII[0], '\n \t' ,self.NatII[1], '\n \t' ,self.NatII[2], '\n')
        return(True)
    def MThemeNatII(self): 
        print('Le thème choisie est -----Nature-----\n')
        print('\t****** Les Sites de Thème Nature sont: *****\n')
        print('\t' ,self.NatII[0], '\n \t',self.NatII[1], '\n \t' ,self.NatII[2],'\n')
        return(True)
        
        
        
        
        
        