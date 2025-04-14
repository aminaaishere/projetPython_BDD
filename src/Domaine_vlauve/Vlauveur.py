class Vlauveur:
    """
    Classe représentant un utilisateur de type "Vlauveur".
    """

    def __init__(self, idVlauveur, email, nom, prenom, adresse, numCarteAbonnement):
        self.idVlauveur = idVlauveur
        self.email = email
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.numCarteAbonnement = numCarteAbonnement
        # self.trajets = []