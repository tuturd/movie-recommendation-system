# Movie Recommendation System
### NF06 - Pratique de la programmation

**Sommaire:**

1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
    - [Respository](#repository)
    - [Python](#python)
3. [Mise à jour des dépendances Python](#3-mise-à-jour-des-dépendances)
4. [Base de donnée](#4-base-de-données)
    - [SQLite3](#sqlite3)
    - [Seeding](#seeding)
    - [Modification du schéma SQL](#mise-à-jour-du-schéma-sql)
    - [Mise à jour des données d'exemple](#mise-à-jour-des-données-dexemple)
5. [Extension C](#5-extension-c)
    - [Compilation](#compilation)
    - [Remise à zéro](#remise-à-zéro)
    - [Paramètres](#paramètres)

<hr>

## 1. Introduction
Il s'agit d'un projet final de NF06 - Pratique de la programmation, unité d'enseignement de l'Université de Technologie de Troyes.

Ce logiciel consiste en un système de recommandation de film basé sur le degré de similitude d'avis entre les utilisateurs.

Vous souhaitez simplement **tester le logiciel** ?
Effectuez les étapes suivantes:
1. [Installation](#2-installation)
2. [SQLite3](#sqlite3)

L'initialisation de la base de donnée sera effectuée directement lors de la première execution du logiciel.

Vous souhaitez **ajouter des fonctionnalités** ? Il est nécessaire d'effectuer toutes les étapes mentionnées dans ce README.

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
- Sur Windows : Pas d'installation nécessaire, la librairie est directement dans [src/c_extension/sqlite3](src/c_extension/sqlite3)

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

### Mise à jour des données d'exemple
Modifier les fichiers .sql (*sauf seed.sql*) dans le dossier [src/database/seed](src/database/seed)

<hr>

## 5. Extension C
Utilisation du module `ctypes` installé par défaut sur Python.
Lien vers la documentation : [ici](https://docs.python.org/3/library/ctypes.html)

### Compilation

Le code C est compilé en extensions Python .so et .dll via le compilateur [gcc](https://www.gnu.org/).
Installation:
- Sur Linux : `sudo apt-get install gcc`

En fonction du système d'exploitation utilisé lors de l'utilisation de l'application, l'extension adéquate sera automatiquement utilisée (.so sur noyau Linux, .dll sous Windows). Il en va de même pour la compilation du code.

> [!WARNING]  
> Cette fonction n'est utilisable que sous Linux pour l'instant

Se déplacer dans [src/c_extension](src/c_extension)

Un script de génération automatique peut être lancé via la commande suivante:
`python extension.py build`

### Remise à zéro

> [!INFO]  
> Se déplacer dans [src/c_extension](src/c_extension)

Pour supprimer les librairies, fichiers de builds et dossiers d'anciennes compilation du code C, entrer la commande suivante:
`python extension.py reset`

### Paramètres

Modifier le fichier [/src/c_extension/utils/settings.json](/src/c_extension/utils/settings.json)