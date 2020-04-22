class ZoneTouristique:
    zone=''
    Zones=['Rabat-Sale','Tiznit']
    def __init__(self,zone):
        self.zone=zone
    def verify(self): 
        return (self.zone in self.Zones)
    


        
        
        
        