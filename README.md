# Movie Recommendation System
### Projet de NF06

**Sommaire:**
1. [Installation](#1-installation)
    - [Respository](#repository)
    - [Python](#python)
    - [Extension C](#extension-c)
2. [Mise à jour des dépendances Python](#2-mise-à-jour-des-dépendances)
3. [Base de donnée](#3-base-de-données)

<hr>

## 1. Installation

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

## Extension C

Se déplacer dans [src/c_extension](src/c_extension)
```
python extension.py reset
python extension.py build
```

<hr>

## 2. Mise à jour des dépendances:

Pour mettre à jour le fichier [requirements.txt](requirements.txt)
> [!WARNING]  
> Il est nécessaire d'avoir activé l'environnement virtuel.

`pip freeze -r requirements.txt`

<hr>

## 3. Base de données:

Utilisation du module `sqlite3` installée par défaut sur Python.
Lien vers la documentation : [ici](https://www.sqlite.org/docs.html)