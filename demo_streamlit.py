import streamlit as st
import pandas as pd

# Exemple de fonction de recommandation
def recommend(brief):
    # Appelle votre système de recommandations
    # Ici, on retourne un exemple statique
    return [
        {"title": "Lieu 1", "activity": "Randonnée", "city": "Paris"},
        {"title": "Lieu 2", "activity": "Dîner", "city": "Lyon"}
    ]

# Titre de l'application
st.title("Système de recommandations de lieux et d'activités")

# Saisie du brief utilisateur
brief = st.text_input("Entrez un brief textuel :")

if st.button("Lancer la recherche"):
    if brief:
        # Appeler le système de recommandations
        results = recommend(brief)
        # Afficher les résultats
        st.write("Résultats :")
        st.write(pd.DataFrame(results))
    else:
        st.warning("Veuillez entrer un brief avant de lancer la recherche.")