from mysql.connector import Error
from DAO.DAOSession import DAOSession

class DAOVille:
    unique_instance = None

    @staticmethod
    def get_instance():
        if DAOVille.unique_instance is None:
            DAOVille.unique_instance = DAOVille()
        return DAOVille.unique_instance

    def insert_ville(self, une_ville):
        sql = "INSERT INTO buveur (idVille, nom,codePostale) VALUES (%s, %s,%s)"
        valeurs = (une_ville.get_idVille(), une_ville.get_nom(),une_ville.get_codePostale)
        try:
            connection = DAOSession.get_connexion()
            cursor = connection.cursor()
            cursor.execute(sql, valeurs)
            cle = cursor.lastrowid
            #print(sql)
            return cle
        except Error as e:
            print("\n<--------------------------------------->")
            print(f"Erreur lors de la création de buveur : {e}")
            print(sql)
            print(valeurs)
            print("rollback")
            connection.rollback() 
            return -1
        finally:
            if cursor:
                cursor.close()

    def delete_buveur(self, une_ville):
        sql = "DELETE FROM buveur WHERE idBuveur = %s"
        valeurs = (un_buveur.get_idBuveur(),)
        try:
            connection = DAOSession.get_connexion()
            cursor = connection.cursor()
            cursor.execute(sql, valeurs)
            return True
        except Error as e:
            print("\n<--------------------------------------->")
            print(f"Erreur lors de la suppression de buveur : {e}")
            print(sql)
            print(valeurs)
            print("rollback")
            connection.rollback() 
            return False
        finally:
            if cursor:
                cursor.close()

    def find_buveur(self, id_buveur):
        sql = "SELECT * FROM buveur WHERE idBuveur = %s"
        valeurs = (id_buveur,)
        try:
            connection = DAOSession.get_connexion()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql, valeurs)
            rs = cursor.fetchone()
            if rs:
                return self.set_all_values(rs)
            else:
                return None
        except Error as e:
            print("\n<--------------------------------------->")
            print(f"Erreur lors de la recherche d'un buveur : {e}")
            print(sql)
            print(valeurs)
            return None
        finally:
            if cursor:
                cursor.close()

    def update_buveur(self, un_buveur):
        sql = "UPDATE buveur SET nom = %s, prenom = %s WHERE idBuveur = %s"
        valeurs = (un_buveur.get_nom(), un_buveur.get_prenom(), un_buveur.get_idBuveur())
        try:
            connection = DAOSession.get_connexion()
            cursor = connection.cursor()
            cursor.execute(sql, valeurs)
            return True
        except Error as e:
            print("\n<--------------------------------------->")
            print(f"Erreur lors de la mise à jour de buveur : {e}")
            print(sql)
            print(valeurs)
            print("rollback")
            connection.rollback() 
            return False
        finally:
            if cursor:
                cursor.close()

    def select_buveur(self, un_buveur):
        les_buveurs = []
        sql = "SELECT * FROM buveur WHERE "
        critere_id = un_buveur.get_idBuveur()
        critere_nom = un_buveur.get_nom()
        critere_prenom = un_buveur.get_prenom()
        valeurs = []

        if critere_id is not None:
            sql += "idBuveur = %s"
            valeurs.append(critere_id)
        elif critere_nom is None and critere_prenom is None:
            sql = "SELECT * FROM buveur"
        else:
            conditions = []
            if critere_nom is not None:
                conditions.append("nom = %s")
                valeurs.append(critere_nom)
            if critere_prenom is not None:
                conditions.append("prenom = %s")
                valeurs.append(critere_prenom)
            sql += " AND ".join(conditions)

        try:
            connection = DAOSession.get_connexion()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(sql, tuple(valeurs))
            rs = cursor.fetchall()
            for row in rs:
                les_buveurs.append(self.set_all_values(row))
        except Error as e:
            print("\n<--------------------------------------->")
            print(f"Erreur lors de la recherche de buveur : {e}")
            print(sql)
            print(valeurs)
        finally:
            if cursor:
                cursor.close()
        return les_buveurs

    def set_all_values(self, rs):
        from DAO.DAOABu import DAOABu
        from domaineVin.ABu import ABu
        from domaineVin.Buveur import Buveur
        un_buveur = Buveur(rs["idBuveur"], rs["nom"], rs["prenom"]) 
        """
         #Chargement des vins bus
        leDAOABu = DAOABu.get_instance()
        les_abus = leDAOABu.select_abu(ABu(idBuveur=un_buveur.get_idBuveur()))
        un_buveur.set_lesDegustations(les_abus)
        """
        return un_buveur