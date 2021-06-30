"""
Le module configparser permet de sauvegarder des données comme 
une base de données de type Sqlite3.
Le recours à ce module par rapport à une base de données est requise
lorsque les données à sauvegarder sont très faibles en quantité.
Cependant, d'un point de vue sécurité / accès aux droits, les bases de 
données sont plus performantes que les fichiers de configuration

Le fichier de configuration (.ini, .cfg...) est constitué de paires :
-> sections
-> champs inclus dans la section
(assimilables aux dictionnaires)

Toutes valeurs dans les champs du fichier de configuration sont des str

Les commentaires sont séparés du ';' ou du '#'

Édition : Laurent REYNAUD
Date : 30-06-2021
"""

from configparser import ConfigParser

# Récupération du fichier .ini
my_test = ConfigParser()
my_test.read('test/test.ini')

# Ajout d'une section dans le fichier .ini
try:
    my_test.add_section('Section3')
    my_test.add_section('Section4')
except:
    print("Sections déjà ajoutés")

# Modification/Ajout de champs du fichier .ini
try: 
    # Modification d'un champ existant
    my_test.set('Section1', 'Champ1', '22')
    # Ajout d'un champ
    my_test.set('Section3', 'Champ4', 'Salut !')
except:
    print("Champs déjà modifiés/ajoutés")

# Suppression d'un champ
try:
    my_test.remove_option('Section2', 'champ3')
except:
    print("Champ déjà supprimé")

# Suppression d'une section
try:
    my_test.remove_section('Section4')
except:
    print("Section déjà supprimée")

# Sauvegarde des données dans le fichier .ini
with open('test/test.ini', 'w') as configfile:
    my_test.write(configfile)
    
# Affichage des sections fichier .ini
print(my_test.sections())

# Afficher le contenu du fichier .ini
read_it = open('test/test.ini', 'r')
content = read_it.read()
print(content)
