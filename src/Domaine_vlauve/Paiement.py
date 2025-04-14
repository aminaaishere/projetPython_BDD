class Paiement:
    """
    Classe représentant un paiement.
    """

    def __init__(self, idPaiement, datePaiement, montant):
        self.idPaiement = idPaiement
        self.datePaiement = datePaiement
        self.montant = montant
        #self.idFacture = idFacture


    def __str__(self):
        return f"Paiement {self.idPaiement} : {self.datePaiement}, {self.montant}"