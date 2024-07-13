from zeep import Client
from zeep.exceptions import Fault

class UtilisateurDAO:
    def __init__(self, wsdl_url):
        self.client = Client(wsdl_url)

    def authenticate_utilisateur(self, email, mot_de_passe):
        print(f"Authenticating with email: {email}, mot_de_passe: {mot_de_passe}")
        try:
            response = self.client.service.authenticateUtilisateur(email, mot_de_passe)
            print(f"Response: {response}")
            return response
        except Fault as fault:
            print(f"Fault occurred: {fault}")
            raise

    def list_utilisateurs(self):
        print("Listing utilisateurs")
        try:
            response = self.client.service.listUtilisateurs()
            print(f"Response: {response}")
            return response
        except Fault as fault:
            print(f"Fault occurred: {fault}")
            raise

    def create_utilisateur(self, nom, email, mot_de_passe, role):
        print(f"Creating utilisateur with nom: {nom}, email: {email}, role: {role}")
        try:
            response = self.client.service.createUtilisateur(nom, email, mot_de_passe, role)
            print(f"Response: {response}")
            return response
        except Fault as fault:
            print(f"Fault occurred: {fault}")
            raise

    def delete_utilisateur(self, id):
        print(f"Deleting utilisateur with id: {id}")
        try:
            response = self.client.service.deleteUtilisateur(id)
            print(f"Response: {response}")
            return response
        except Fault as fault:
            print(f"Fault occurred: {fault}")
            raise

    def update_utilisateur(self, id, data):
        print(f"Updating utilisateur with id: {id}, data: {data}")
        try:
            response = self.client.service.updateUtilisateur(id, data)
            print(f"Response: {response}")
            return response
        except Fault as fault:
            print(f"Fault occurred: {fault}")
            raise
