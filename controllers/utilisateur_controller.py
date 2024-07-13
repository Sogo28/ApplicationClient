from services.utilisateur_service import UtilisateurService

class UtilisateurController:
    def __init__(self, wsdl_url):
        self.utilisateur_service = UtilisateurService(wsdl_url)

    def authenticate(self, email, mot_de_passe):
        return self.utilisateur_service.authenticate(email, mot_de_passe)

    def list_utilisateurs(self):
        return self.utilisateur_service.list_utilisateurs()

    def create_utilisateur(self, nom, email, mot_de_passe, role):
        return self.utilisateur_service.create_utilisateur(nom, email, mot_de_passe, role)

    def delete_utilisateur(self, id):
        return self.utilisateur_service.delete_utilisateur(id)

    def update_utilisateur(self, id, data):
        return self.utilisateur_service.update_utilisateur(id, data)
