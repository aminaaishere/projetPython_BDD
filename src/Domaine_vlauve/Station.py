class Station :
    def __init__(self, numStation, nom, coordonnees_GPS, numRue, nomRue, nbplacesElec, nbplacesNElec, vlElecDispo, vlNElecDispo)  :
        self.numStation = numStation
        self.nom = nom
        self.coordonnees_GPS = coordonnees_GPS
        self.numRue = numRue
        self.nomRue = nomRue
        self.nbplacesElec = nbplacesElec
        self.nbplacesNElec = nbplacesNElec  
        self.vlElecDispo = vlElecDispo
        self.vlNElecDispo = vlNElecDispo
        #self.idReseau = idReseau

    def __str__(self) : 
        return f"Station {self.nom} : {self.coordonnees_GPS}, {self.numRue}, {self.nomRue}, {self.nbplacesElec}, {self.nbplacesNElec}, {self.vlElecDispo}, {self.vlNElecDispo}"