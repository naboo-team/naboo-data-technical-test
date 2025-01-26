import pandas as pd

from src.data_processing import load_data, clean_data
from src.recommendation_system import extract_info_from_brief, recommend

def main(brief):
    # Charger et nettoyer les données
    services_activities, service_providers, venues = load_data()
    services_activities, service_providers, venues = clean_data(services_activities, service_providers, venues)
    
    # Using a standardised approach for simple business rules
    requirements = pd.read_csv('./data/requirements.csv')

    # Extraire les informations du brief
    brief_info = extract_info_from_brief(brief, requirements)
    
    # Obtenir les recommandations
    recommendations = recommend(services_activities, service_providers, venues, brief_info, requirements)
    
    return recommendations

if __name__ == "__main__":
    brief = "Je cherche une activité dynamique à Paris pour un groupe de 10 personnes."
    results = main(brief)
    print(results)
   