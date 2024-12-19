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

Se placer à la racine du repository, branche `dev`.

Le repository est organisé comme suit:
- `dev`: developpement de nouvelles fonctionnalitées, correctifs
- `master`: version stable de l'application


## Python

Tout d'abord installer python3.10: [téléchargeable ici](https://www.python.org/downloads/)

Configurer ensuite l'environnement virtuel Python
`python -m venv .venv`

Activer l'environnement virtuel
- Sur Linux/Mac : `source .venv/bin/activate`
- Sur Windows : `.venv\Scripts\activate`
s
Installer les librairies nécessaires
```
# Pour les modules Python
pip install -r requirements.txt

# Installation de Tkinter sous Linux
sudo apt install python3-tk

# Installation de Tkinter sous Windows
pip install tk

```

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

Installation pour C
- Sur Linux : `sudo apt-get install libsqlite3-dev`

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
Utilisation du module `ctypes` installée par défaut sur Python.
Lien vers la documentation : [ici](https://docs.python.org/3/library/ctypes.html)

Se déplacer dans [src/c_extension](src/c_extension)

### Compilation
Le code C est compilé en extension Python .so via le compilateur [gcc](https://www.gnu.org/).
Un script de génération automatique peut être lancé via la commande suivante:
`python extension.py build`

### Remise à zéro
Pour supprimer les librairies, fichiers de builds et dossiers d'anciennes compilation du code C, entrer la commande suivante:
`python extension.py reset`

### Paramètres
Modifier le fichier [/src/c_extension/utils/settings.json](/src/c_extension/utils/settings.json)