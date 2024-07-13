from views.gui import Application

if __name__ == "__main__":
    wsdl_url = "http://localhost:4000/wsdl?wsdl"  # URL du service SOAP
    app = Application(wsdl_url)
    app.mainloop()
