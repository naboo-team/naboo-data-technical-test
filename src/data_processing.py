import pandas as pd

def load_data():
    """
    Charge les fichiers CSV de données (places, providers, services) dans des DataFrames pandas.
    """
    places = pd.read_csv('places.csv')
    service_providers = pd.read_csv('service_providers.csv')
    services = pd.read_csv('services.csv')
    
    return places, service_providers, services

def clean_data(places, service_providers, services):
    """
    Effectue un nettoyage basique des données si nécessaire. Par exemple, enlever les doublons,
    vérifier les valeurs manquantes, ou normaliser les chaînes de texte.
    """
    places.drop_duplicates(inplace=True)
    service_providers.drop_duplicates(inplace=True)
    services.drop_duplicates(inplace=True)
    
    # D'autres opérations de nettoyage peuvent être ajoutées ici si nécessaire
    return places, service_providers, services

# Example of usage
# places, providers, services = load_data()
# places, providers, services = clean_data(places, providers, services)