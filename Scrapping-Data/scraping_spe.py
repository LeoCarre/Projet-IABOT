import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fonction pour extraire les données des spécialités
def extract_specialties(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    specialties = []

    # Trouver toutes les sections de spécialités
    sections = soup.find_all('div', {'class': 'faq-section__accordion'})

    for section in sections:
        # Trouver le titre de la section (Les spécialités de la voie générale / Les séries de la voie technologique)
        title = section.find('h3', {'class': 'faqfield-question on_summary'}).text.strip()

        # Trouver les spécialités dans la section
        specialties_list = section.find_all('h4', {'class': 'title'})
        specialties_names = [specialty.text.strip() for specialty in specialties_list]

        # Ajouter les données extraites à la liste
        specialties.append({'Title': title, 'Specialties': ', '.join(specialties_names)})

    return specialties

# URL de la page Web
url = "https://www.education.gouv.fr/reussir-au-lycee/choisir-ses-enseignements-de-specialite-au-lycee-pour-preparer-ses-etudes-superieures-325475"

# Extraire les spécialités
specialties_data = extract_specialties(url)

# Créer un DataFrame à partir des données
df = pd.DataFrame(specialties_data)

# Enregistrer le DataFrame dans un fichier CSV
df.to_csv('specialties_data.csv', index=False)

print("Les données ont été extraites et enregistrées dans le fichier CSV.")
