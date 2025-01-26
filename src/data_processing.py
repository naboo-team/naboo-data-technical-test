
import pandas as pd

def load_data():
    """
    Charge les fichiers CSV de données (services_activities, providers, venues) dans des DataFrames pandas.
    """
    services_activities = pd.read_csv('./data/services_activities.csv')
    service_providers = pd.read_csv('./data/service_providers.csv')
    venues = pd.read_csv('./data/venues.csv')

    return services_activities, service_providers, venues

def clean_data(services_activities, service_providers, venues):
    """
    Effectue un nettoyage basique des données si nécessaire. Par exemple, enlever les doublons,
    vérifier les valeurs manquantes, ou normaliser les chaînes de texte.
    """

    services_activities.drop_duplicates(inplace=True)
    service_providers.drop_duplicates(inplace=True)
    venues.drop_duplicates(inplace=True)

    services_activities = services_activities.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    service_providers = service_providers.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    venues = venues.applymap(lambda x: x.lower() if isinstance(x, str) else x)
    
    # D'autres opérations de nettoyage peuvent être ajoutées ici si nécessaire
    return services_activities, service_providers, venues

# Example of usage
# services_activities, providers, venues = load_data()
# services_activities, providers, venues = clean_data(services_activities, providers, venues)