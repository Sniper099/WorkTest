class SiteTouristique():
    ZnST={}
    ZnST={'Rabat-Salé':['Tour Hassan','Oudaya,Chellah','Le Musée Mohammed VI','Musée Belghazi','Musée Maroc Télécom','Village de poterie Oulja','Ancienne Médina Rabat','Oued Bouregreg','Jardin exotique'],'Tiznit':['Ein Zarqa','Mirleft','Quissariat Neqra','Ouad Assaka','Targa','Sidi Boulfdayl','Al Aqwass','Qasr Khalifi']}
    ZoneSelect=''
    def __init__(self,ZoneSelect):
        self.ZoneSelect=ZoneSelect
    def SitesDZones(self):
        if self.ZoneSelect=='Rabat-Salé' :
            return(self.ZnST['Rabat-Salé'])
        else:
            return(self.ZnST['Tiznit'])

    