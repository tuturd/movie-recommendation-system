# Movie Recommendation System
### NF06 - Pratique de la programmation

**Sommaire:**

1. [Introduction](#1-introduction)
2. [Installation](#1-installation)
    - [Respository](#repository)
    - [Python](#python)
3. [Mise à jour des dépendances Python](#2-mise-à-jour-des-dépendances)
4. [Base de donnée](#3-base-de-données)
    - [SQLite3](#sqlite3)
    - [Seeding](#seeding)
    - [Modification du schéma SQL](#mise-à-jour-du-schéma-sql)
5. [Extension C](#4-extension-c)
    - [Compilation](#compilation)
    - [Remise à zéro](#remise-à-zéro)
    - [Paramètres](#paramètres)

<hr>

## 1. Introduction
> à compléter

<hr>

## 2. Installation

## Repository

Installer le repository
`git clone https://github.com/tuturd/movie-recommendation-system.git`

Se placer à la racine du repository.


## Python

Tout d'abord installer python3.10: [téléchargeable ici](https://www.python.org/downloads/)

Configurer ensuite l'environnement virtuel Python
`python -m venv .venv`

Activer l'environnement virtuel
- Sur Linux : `source .venv/bin/activate`
- Sur Windows : `.venv\Scripts\activate`

Installer les librairies nécessaires
`pip install -r requirements.txt`

<hr>

## 3. Mise à jour des dépendances:

Pour mettre à jour le fichier [requirements.txt](requirements.txt)
> [!WARNING]  
> Il est nécessaire d'avoir activé l'environnement virtuel.

`pip freeze > requirements.txt`

<hr>

## 4. Base de données:

### SQLite3
Utilisation du module `sqlite3` installée par défaut sur Python.
Lien vers la documentation : [ici](https://www.sqlite.org/docs.html)

### Seeding
Se déplacer dans [src/database](src/database)
```
# Pour créer la db
python database.py seed

# Pour ajouter des données d'exemple
python database.py example_data
```

### Mise à jour du schéma SQL
Modifier [src/database/seed/seed.sql](src/database/seed/seed.sql)

<hr>

## 5. Extension C
Se déplacer dans [src/c_extension](src/c_extension)

### Compilation
`python extension.py build`

### Remise à zéro
`python extension.py reset`

### Paramètres
Modifier le fichier [/src/c_extension/utils/settings.json](/src/c_extension/utils/settings.json)