# Dispositif numérique de cartographie culturelle à Lavaux

**Auteur : Joseph Grob**  
**Contact : joseph.grob@unil.ch**

Ce dépôt contient les fichiers et ressources liés au mémoire de master consacré à l'exploration d’un dispositif numérique pour la sauvegarde du patrimoine culturel immatériel (PCI), appliqué au cas des murs de vigne à Lavaux.

## Objectif du dispositif

Ce projet expérimental vise à :

- Représenter spatialement les dimensions invisibles du patrimoine immatériel
- Documenter son évolution dans le temps
- Impliquer les communautés locales dans une démarche participative
- Offrir une lecture sensible, située et relationnelle du PCI

## Fonctionnement général

Le dispositif est structuré autour de trois étapes principales :

1. **Collecte participative**  
   Les participants sont invités à remplir un formulaire numérique (`index.html`). Ils y décrivent une pratique patrimoniale, une mémoire ou un savoir-faire lié à Lavaux, ainsi que des informations géographiques et sociales. Ces données sont automatiquement enregistrées dans une base en ligne (via [Baserow](https://baserow.io)).

2. **Traitement des données**  
   Des scripts Python permettent d’analyser les données collectées :
   - Extraction depuis l’API Baserow (`get_data_baserow.py`)
   - Traitement des contenus, regroupement des pratiques, analyse automatique (`analyse_auto.py`, `clusters_pratique.py`)
   - Format RDF sémantique pour tests de structuration et interopérabilité (`rdf_export.py`)

3. **Visualisation**  
   Le fichier `network_test.html` permet de visualiser dynamiquement le réseau d’acteurs, de pratiques et de lieux. Il met en évidence les liens entre les répondants, les types de savoirs, et leur ancrage territorial.

Chaque étape est documentée et accessible individuellement à travers ce dépôt.

## Contenu du dépôt

Le dossier contient les éléments suivants :

### Interfaces HTML

- [`index.html`](index.html) : Formulaire interactif de collecte des données patrimoniales  
- [`network_test.html`](network_test.html) : Visualisation dynamique du réseau de savoirs et de pratiques  

### Scripts Python

- [`analyse_auto.py`](analyse_auto.py) : Analyse automatique des données patrimoniales  
- [`clusters_pratique.py`](clusters_pratique.py) : Algorithme de regroupement des pratiques  
- [`get_data_baserow.py`](get_data_baserow.py) : Extraction de données depuis l’API Baserow  

### RDF (prototype sémantique)

- [`rdf_export.py`](rdf_export.py) : Exemple d’export RDF utilisant les vocabulaires SKOS et CIDOC CRM  

## Accès aux visualisations et interfaces

Ces fichiers sont consultables localement ou via GitHub Pages :

- Formulaire de collecte : [Ouvrir](https://josephgrob.github.io/pci-cartographie-lavaux/index.html)
- Visualisation réseau : [Ouvrir](https://josephgrob.github.io/pci-cartographie-lavaux/network_test.html)
- Données en ligne (Baserow) : https://baserow.io/public/grid/9qKrvm3TS3b9LcambCqkfOeBHrougPpvHNBARHzU2NM

## Accès à distance

Le dépôt complet est disponible publiquement ici :

🔗 [https://github.com/JosephGrob/pci-cartographie-lavaux](https://github.com/JosephGrob/pci-cartographie-lavaux)

## Licence

Ce projet est proposé à des fins pédagogiques dans le cadre d’un mémoire universitaire. Toute réutilisation doit mentionner la source.

## Remarques

- Les données utilisées dans ce dépôt sont **fictives**.
- En cas d’application réelle, des mesures de protection des données personnelles (anonymisation, consentement, etc.) devront être mises en place.
- Ce dépôt n’inclut pas les fichiers de visualisation ou scripts non essentiels à la démonstration du dispositif.
