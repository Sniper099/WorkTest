from PackDATA.MonumentHistorique import MonumentHistorique
from PackDATA.Musee import Musee
from PackDATA.SiteProduction import SiteProduction
from PackDATA.SiteNatRemrq import SiteNatRemrq
from PackDATA.SiteTouristique import SiteTouristique
from PackDATA.ZoneTouristique import ZoneTouristique
from PackDATA.SiteVisite import SiteVisite
#Affichage des zones
def AffZone():
    print('********************************* Les Zones diponibles sur notre gestionnaire *********************************\n')
    print('\t La Zone Touristique de Rabat-Sale \n \t La Zone Touristique de Tiznit\n')
    
#Selection de zone
def SelectZone(om):
    Zonee=ZoneTouristique(om)
    if (Zonee.verify()):
        print('----------La Zone Touristique choisie est La Zone de :', om, '\n')
        return(om)
    else:
        print('Veuillez choisir une zone parmis les zone disponibles SVP!')
        return('Erreur')
    
#Affichage de sites de zone
def AffSites(zon):
    Sitee=SiteTouristique(zon)
    S=Sitee.SitesDZones()
    for i in S :
        print('>>>Site Touristique : ',i,)
    return(True)
    
#Affichage de sites selon la catégorie
def Category(zon):
    if (zon=='Rabat-Sale'):
        Monn=MonumentHistorique(zon)
        Monn.MCategoryI()
        Muss=Musee(zon)
        Muss.MuCategoryI()
        Prodd=SiteProduction(zon)
        Prodd.PCategoryI()
        Natt=SiteNatRemrq(zon)
        Natt.NCategoryI()
    elif(zon=='Tiznit'):
        Monn=MonumentHistorique(zon)
        Monn.MCategoryII()
        Prodd=SiteProduction(zon)
        Prodd.PCategoryII()
        Natt=SiteNatRemrq(zon)
        Natt.NCategoryII()
    return(True)

#Affichage de sites selon le thème
def Theme(zon):
    if(zon=='Rabat-Sale'):
        Monn=MonumentHistorique(zon)
        Monn.MThemeHistoryI()
        Muss=Musee(zon)
        Muss.MThemeArtI()
        Muss.MThemeEthnoI()
        Muss.MThemeTelecomI()
        Prodd=SiteProduction(zon)
        Prodd.MThemeArtI()
        Natt=SiteNatRemrq(zon)
        Natt.MThemeNatI()
    elif(zon=='Tiznit'):
        Monn=MonumentHistorique(zon)
        Monn.MThemeHistoryII()
        Prodd=SiteProduction(zon)
        Prodd.MThemeArtII()
        Natt=SiteNatRemrq(zon)
        Natt.MThemeNatII()
    return(True)
    
#Affichage des sites qui proposent des visites guidées
def Visite(zon):
    if(zon=='Rabat-Sale'):
        Vis=SiteVisite()
        Vis.VisiteI()
    elif(zon=='Tiznit'):
        print('La Zone Touristique de TIZNIT ne propose aucune visite guidée \n')
    return(True)
        