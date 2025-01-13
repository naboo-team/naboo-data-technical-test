from data_processing import load_data, clean_data
from recommendation_system import extract_info_from_brief, recommend

def main(brief):
    # Charger et nettoyer les données
    places, providers, services = load_data()
    places, providers, services = clean_data(places, providers, services)
    
    # Extraire les informations du brief
    brief_info = extract_info_from_brief(brief)
    
    # Obtenir les recommandations
    recommendations = recommend(places, providers, services, brief_info)
    
    return recommendations

if __name__ == "__main__":
    brief = "Je cherche une activité dynamique à Paris pour un groupe de 10 personnes."
    results = main(brief)

    # Afficher les recommandations
    # ...
   