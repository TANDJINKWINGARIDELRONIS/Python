
# 🧮 Calculatrice Scientifique en Python (Tkinter)

## 📘 Description

Cette application est une **calculatrice scientifique complète** développée en **Python** à l’aide de la bibliothèque **Tkinter** pour l’interface graphique.  
Elle propose deux modes d’utilisation :

- **Mode Standard** : pour les opérations de base (+, −, ×, ÷)
- **Mode Scientifique** : pour les fonctions avancées (trigonométriques, logarithmiques, puissances, exponentielles, etc.)

---

## 🚀 Fonctionnalités

### 🔹 Mode Standard
- Addition, soustraction, multiplication, division  
- Effacer un chiffre (`C`) ou tout effacer (`CE`)  
- Changement de signe (`±`)  
- Racine carrée (`√`)  
- Affichage clair et dynamique  

### 🔹 Mode Scientifique
- Fonctions trigonométriques : `sin`, `cos`, `tan`, `sinh`, `cosh`, `tanh`
- Fonctions inverses : `1/x`
- Puissances : `x²`, `x³`, `xʸ`
- Logarithmes : `log`, `log2`
- Constantes : `π`, `2π`, `e`
- Fonctions hyperboliques inverses : `asinh`, `acosh`
- Conversion degrés ↔ radians (`°`)
- Exponentielle (`exp`)
- Modulo (`%`)
- Effet de bascule entre **calculatrice standard** et **scientifique**

---

## 🧠 Structure du Code

### 1. **Interface Graphique (Tkinter)**
- Fenêtre principale (`Tk()`)
- Cadre (`Frame`) pour contenir les boutons et l’écran
- Menu avec :
  - **Fichier** : changer le mode / quitter  
  - **Édition** : couper, copier, coller  
  - **Aide** : obtenir de l’aide

### 2. **Classe `Calculator`**
Cette classe gère toute la logique de calcul :
- Gestion des entrées clavier (`input_number`)
- Calculs et opérateurs (`operator`, `valid_function`, `sum_of_total`)
- Fonctions mathématiques (`sqrt`, `sin`, `log`, `exp`, etc.)
- Fonctions de gestion d’affichage (`display`, `clear`, `clear_all`)

### 3. **Boutons**
Les boutons numériques et fonctionnels sont générés dynamiquement :
```python
numberlist = "789456123"
for i in range(2,5):
    for j in range(3):
        Button(..., text=numberlist[k], command=lambda x=numberlist[k]: added_value.input_number(x))
```

---

## 🛠️ Installation et Exécution

### ✅ Prérequis
- Python 3.x installé sur votre machine
- Bibliothèque Tkinter (généralement installée par défaut avec Python)

### ▶️ Exécution
1. Téléchargez le fichier `calculatrice_scientifique.py`
2. Exécutez la commande suivante dans un terminal :
   ```bash
   python calculatrice_scientifique.py
   ```
3. La calculatrice s’ouvrira dans une nouvelle fenêtre.

---

## 🧩 Navigation dans les menus

| Menu | Options | Description |
|------|----------|-------------|
| **Fichier** | `standard`, `scientific`, `Exit` | Changer le mode ou quitter |
| **Éditer** | `Couper`, `Copier`, `Coller` | Gestion du presse-papiers |
| **Aide** | `Obtenir de l’aide` | Affiche une aide simple |

---

## 🖼️ Aperçu

```
┌───────────────────────────────────────────┐
│ Scientific Calculator                     │
│───────────────────────────────────────────│
│ [Écran d’affichage des résultats]         │
│-------------------------------------------│
│ [Boutons standard : chiffres + opérations]│
│-------------------------------------------│
│ [Boutons scientifiques : sin, log, exp...]│
└───────────────────────────────────────────┘
```

---

## 🧑‍💻 Auteur

**Projet réalisé par :** MOSTWANTED  
📅 **Année :** 2025  
💡 **Langage :** Python (Tkinter)

---

## ⚙️ Licence

Ce projet est libre d’utilisation à des fins éducatives ou personnelles.  
Toute reproduction à but commercial nécessite l’autorisation de l’auteur.

---

## ❤️ Remerciements

Merci à la communauté Python pour la documentation et le soutien, ainsi qu’à Tkinter pour sa simplicité d’utilisation.

---
