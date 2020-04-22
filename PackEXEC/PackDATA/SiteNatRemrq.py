from PackDATA.ZoneTouristique import ZoneTouristique 
class SiteNatRemrq(ZoneTouristique):
    Nat=['Village de poterie Oulja','Ancienne Medina Rabat']
    NatII=['Mirleft','Ouad Assaka','Targa']
    nat=''
    zone=''
    def __init__(self,zone,nat='Categorie Site Naturel Remarquable'):
        ZoneTouristique.__init__(self,zone)
        self.nat=nat
    def NCategoryI(self): 
        print('La categorie----- Site Naturel Remarquable-----\n')
        print('\t****** Les Sites de Categorie Site Naturel Remarquable sont: *****\n')
        print('\t >', self.Nat[0], '\n \t >' ,self.Nat[1], '\n ')
        return(True)
    def MThemeNatI(self): 
        print('Le theme-----Nature-----\n')
        print('\t****** Les Sites de Theme Nature sont: *****\n')
        print('\t >', self.Nat[0],' \n \t >' ,self.Nat[1], '\n ')
        return(True)
    def NCategoryII(self): 
        print('La categorie----- Site Naturel Remarquable-----\n')
        print('\t****** Les Sites de Categorie Site Naturel Remarquable sont: *****\n')
        print('\t >', self.NatII[0], '\n \t >' ,self.NatII[1], '\n \t >' ,self.NatII[2], '\n')
        return(True)
    def MThemeNatII(self): 
        print('Le theme-----Nature-----\n')
        print('\t****** Les Sites de Theme Nature sont: *****\n')
        print('\t >' ,self.NatII[0], '\n \t >',self.NatII[1], '\n \t >' ,self.NatII[2],'\n')
        return(True)
        

        
        
        
        
        