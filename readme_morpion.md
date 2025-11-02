# 🎮 MORPION 5x5 (Jeu du Tic-Tac-Toe)

Un jeu de **Morpion (Tic-Tac-Toe)** développé en **Python** avec la
bibliothèque **Tkinter**, jouable à deux sur une grille **5x5**.

------------------------------------------------------------------------

## 🧠 Description

Ce projet propose une version améliorée du célèbre jeu du Morpion.\
Deux joueurs s'affrontent à tour de rôle sur une **grille 5x5**.\
Le premier à aligner **5 symboles identiques (X ou O)** horizontalement,
verticalement ou en diagonale remporte la partie.

------------------------------------------------------------------------

## ⚙️ Fonctionnalités

✅ Interface graphique intuitive (Tkinter)\
✅ Jeu à deux joueurs (X et O)\
✅ Système de détection automatique de victoire\
✅ Gestion des matchs nuls\
✅ Fonction *Annuler le dernier coup (Undo)*\
✅ Réinitialisation de la partie (*New Game*)\
✅ Menu d'aide et d'informations\
✅ Message de fin de partie (victoire ou match nul)\
✅ Prévention des clics multiples sur la même case

------------------------------------------------------------------------

## 🕹️ Règles du jeu

-   Le joueur **X** commence toujours la partie.\
-   Les joueurs cliquent tour à tour sur une case vide pour y placer
    leur symbole.\
-   Le premier joueur à aligner **5 symboles identiques** gagne la
    partie.\
-   Si toutes les cases sont remplies sans qu'il y ait de gagnant, la
    partie se termine par un **match nul**.

------------------------------------------------------------------------

## 📜 Structure du code

  Fonction        Description
  --------------- ------------------------------------------------------------
  `clic(i, j)`    Gère le clic sur une case du plateau.
  `unclic()`      Permet d'annuler le dernier coup joué.
  `victoire()`    Vérifie si un joueur a aligné 5 symboles.
  `match_nul()`   Vérifie si le plateau est plein sans vainqueur.
  `fin()`         Désactive toutes les cases lorsque la partie est terminée.
  `reset()`       Réinitialise le plateau pour une nouvelle partie.
  `aide()`        Affiche les règles du jeu.
  `infos()`       Donne les informations sur le jeu et sa version.
  `quitter()`     Ferme proprement l'application.

------------------------------------------------------------------------

## 🧩 Technologies utilisées

-   **Langage :** Python 3\
-   **Bibliothèque :** Tkinter (interface graphique)

------------------------------------------------------------------------

## 🚀 Installation et exécution

### 1️⃣ Installer Python

Assure-toi d'avoir Python 3 installé sur ton système.\
[👉 Télécharger Python ici](https://www.python.org/downloads/)

### 2️⃣ Exécuter le programme

Ouvre un terminal dans le dossier du fichier et exécute :

``` bash
python morpion_5x5.py
```

------------------------------------------------------------------------

## 🧑‍💻 Auteur

👤 **Développeur :** MOSTWANTED\
📘 **Version :** 1.0\
🧠 **Langage :** Python\
📅 **Année :** 2025

------------------------------------------------------------------------

## 📸 Aperçu

-   Une fenêtre Tkinter s'ouvre avec un plateau **5x5**.\
-   En haut, un menu propose :
    -   **Fichier → New Game / Exit**\
    -   **Option → Undo / Aide / À propos**

------------------------------------------------------------------------

## 💡 Améliorations possibles

-   Ajouter un **mode joueur vs ordinateur (IA)**\
-   Ajouter un **scoreboard** pour compter les victoires\
-   Améliorer le design du plateau avec des couleurs dynamiques

------------------------------------------------------------------------


