class SiteTouristique():
    ZnST={}
    ZnST={'Rabat-Sale':['Tour Hassan','Oudaya','Chellah','Le Musee Mohammed VI','Musee Belghazi','Musee Maroc Telecom','Village de poterie Oulja','Ancienne Medina Rabat','Oued Bouregreg','Jardin exotique'],'Tiznit':['Ein Zarqa','Mirleft','Quissariat Neqra','Ouad Assaka','Targa','Sidi Boulfdayl','Al Aqwass','Qasr Khalifi']}
    ZoneSelect=''
    def __init__(self,ZoneSelect):
        self.ZoneSelect=ZoneSelect
    def SitesDZones(self):
        if self.ZoneSelect=='Rabat-Sale' :
            return(self.ZnST['Rabat-Sale'])
        else:
            return(self.ZnST['Tiznit'])

    