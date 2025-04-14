class Abonnement :
    """
    Classe Abonnement
    Attributs :
        - idAbonnement : int
        - type : EType
        - typeAnn : EAnnuel
        - typeOcc : EOccasionnel
        - montantGarantie : float
        - idVlaiveur : int
    """
    def __init__(self, idAbonnement, type, typeAnn, typeOcc, montantGarantie):
        self.idAbonnement = idAbonnement
        self.type = type
        self.typeAnn = typeAnn
        self.typeOcc = typeOcc
        self.montantGarantie = montantGarantie

    def __str__(self):
        return f"Abonnement {self.idAbonnement} : {self.type}, {self.typeAnn}, {self.typeOcc}, {self.montantGarantie}"