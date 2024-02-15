# Projet d'orientation professionnelle

## Contexte

Le projet consiste à créer un chatbot qui pourra aider les étudiants à choisir les spécialités nécessaires pour atteindre le métier de leurs rêves.

## Déroulement

Le travail a commencé par le chargement de deux fichiers CSV, contenant respectivement des informations sur différents métiers et des informations sur les spécialités nécessaires pour ces métiers. Les données du premier CSV, 'all_job_data.csv', étaient composées des caractéristiques des métiers, y compris le titre du métier, la description du métier, les compétences requises et le salaire, parmi d'autres. Le deuxième fichier CSV, 'data - Sheet1.csv', contenait les noms des spécialités.

L'objectif était de créer une correspondance entre les métiers et les spécialités en se basant sur les informations disponibles. Pour ce faire, une nouvelle colonne 'Specialty' a été ajoutée à 'all_job_data.csv', en fonction des informations du 'data - Sheet1.csv'. 

Ensuite, deux autres colonnes, 'Première générale' et 'Première Technologique', ont été créées contenant les spécialités recommandées pour chaque métier pour ces deux séries spécifiques d'études.

Finalement, toutes les informations de chaque métier ont été fusionnées en une seule colonne pour faciliter l'utilisation dans un chatbot.

## Résultats

Les résultats du processus sont disponibles sous forme de fichiers CSV contenant les métiers ainsi que leur correspondance avec les spécialités. Ces fichiers CSV peuvent être utilisés comme entrée pour le chatbot.

## Limites et perspectives

L'approche actuelle d'analyse de texte brute pourrait ne pas capter parfaitement la correspondance entre les métiers et les spécialités. Une analyse plus sophistiquée, qui prend en compte la sémantique et le contexte des mots, pourrait donner des correspondances plus précises.