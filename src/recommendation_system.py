from transformers import pipeline
import pandas as pd

def extract_info_from_brief(brief, requirements):
    """
    Extrait les informations pertinentes d'un brief textuel.
    Cela peut inclure la localisation, le type d'activité, et autres contraintes.
    """
    # Code d'extraction d'informations de base à partir du brief
    # Exemple de sortie : {'location': 'Paris', 'activity_type': 'dynamique', 'group_size': 10}
    # Implémenter l'extraction (par exemple avec des expressions régulières ou NLP)

    pipeline_model = pipeline("text2text-generation", model="google/flan-t5-base")

    # lets consider event details as simple requirements on which we build a standardise extraction logic. This should fasten the implementation of new details in the futur.
    info = {}
    set_of_requirements = requirements['requirement_textual_name']

    # by using a better API maybe it would be possible to avoid doing multiple calls but this one did not permit to get clean JSON results when calling for multiple features at once.
    for requirement in set_of_requirements:

        instruction_city = f"Extract the {requirement} from the following text."

        prompt_city = f"""
            {instruction_city}

            Text: {brief}
        """
        result_city = pipeline_model(prompt_city, max_length=100, clean_up_tokenization_spaces=True)
        
        output_city = result_city[0]["generated_text"].lower()

        # we store each extraction in a json
        info[requirement] = output_city

    return info

def recommend(services_activities, service_providers, venues, brief_info, requirements):
    """
    Recommande des lieux et des activités en fonction du brief textuel analysé.
    """
    type_mapping = {
        'int': int,
        'float': float,
        'str': str,
    }

    recommendations = venues

    # for each requirement we go through the venues and decide if we should exclude them from the reco or increase their score
    for index, requirement in requirements.iterrows():

        recommendations['score'] = 0

        #storing requirements detail into variables
        requirement_name = requirement['requirement_name']
        requirement_textual_name = requirement['requirement_textual_name']
        operator = requirement['operation']
        type = requirement['type']
        requirement_value = brief_info[requirement_textual_name]

        converted_value = type_mapping[type](requirement_value)

        if requirement['priority'] == 0: # meaning the requirement is not an option

            filter_operation = f"recommendations[(recommendations['{requirement_name}']) {operator} converted_value]"
            recommendations = eval(filter_operation)

        elif requirement['priority'] == 1: # it increases the priority of the recommendation

            scoring_operation = f"(row['{requirement_name}'] {operator} {converted_value})"
            recommendations['score'] = recommendations.apply(lambda row: row['score'] + 1 if eval(scoring_operation) else row['score'], axis = 1)

    recommendations = recommendations.sort_values(by='score', ascending=False) # ordering by score
    recommendations = recommendations[['introduction', 'food', 'activities', 'city', 'ambiance', 'capacity', 'house_type']] # keeping interesting details to display
    recommendations = recommendations.head(10) # limiting the display amount
    
    # Filtrer les lieux et les prestataires en fonction des informations extraites du brief
    # Exemple : filtres sur la localisation, le type d'activité, la capacité du groupe, etc.
    
    return recommendations