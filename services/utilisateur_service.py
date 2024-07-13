from model.DAO.utilisateur_dao import UtilisateurDAO

class UtilisateurService:
    def __init__(self, wsdl_url):
        self.dao = UtilisateurDAO(wsdl_url)

    def authenticate(self, email, mot_de_passe):
        return self.dao.authenticate_utilisateur(email, mot_de_passe)

    def list_utilisateurs(self):
        return self.dao.list_utilisateurs()

    def create_utilisateur(self, nom, email, mot_de_passe, role):
        return self.dao.create_utilisateur(nom, email, mot_de_passe, role)

    def delete_utilisateur(self, id):
        return self.dao.delete_utilisateur(id)

    def update_utilisateur(self, id, data):
        return self.dao.update_utilisateur(id, data)
