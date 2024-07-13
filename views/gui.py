import tkinter as tk
from tkinter import messagebox
from controllers.utilisateur_controller import UtilisateurController

class Application(tk.Tk):
    def __init__(self, wsdl_url):
        super().__init__()
        self.title("Gestion des Utilisateurs")
        self.geometry("400x300")
        
        self.utilisateur_controller = UtilisateurController(wsdl_url)
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Email").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self, text="Mot de Passe").grid(row=1, column=0, padx=10, pady=10)
        
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.login_button = tk.Button(self, text="Se Connecter", command=self.authenticate)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    
    def authenticate(self):
        email = self.email_entry.get()
        mot_de_passe = self.password_entry.get()
        
        try:
            auth_response = self.utilisateur_controller.authenticate(email, mot_de_passe)
            if auth_response.auth:
                messagebox.showinfo("Succès", "Authentification réussie")
                # Proceed to the next step, such as opening a new window for user management
            else:
                messagebox.showerror("Erreur", "Échec de l'authentification")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    wsdl_url = "http://localhost:4000/wsdl"
    app = Application(wsdl_url)
    app.mainloop()
