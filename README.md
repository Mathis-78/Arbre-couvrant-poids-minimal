# Arbre couvrant de poids minimal

Ce programme est un de mes **premiers projets en algorithmique**, réalisé **au lycée**.  
Il s’agit d’une implémentation simple (et visuelle) d’un **algorithme d’arbre couvrant de poids minimal**, c’est-à-dire un réseau reliant plusieurs points avec **le moins de distance totale possible**.  
Le but était de comprendre comment **relier des points sans créer de cycles** tout en minimisant la longueur totale des segments.

---

## Description du projet

Le script permet :
- de **générer des points aléatoires** dans un plan 2D ;
- de **calculer les distances** entre tous les couples possibles de points ;
- de **sélectionner les connexions les plus courtes** en évitant les boucles ;
- d’**afficher progressivement le graphe** (avec `matplotlib`), montrant la construction de l’arbre étape par étape.

Ce programme s’appuie sur une logique proche de l’**algorithme de Kruskal**, bien qu’écrit à la main et de manière non optimisée à l’époque.

---

## Technologies utilisées

- **Python 3**
- **NumPy** — pour la manipulation des coordonnées
- **Matplotlib** — pour la visualisation graphique
- **itertools** — pour générer les combinaisons de connexions possibles
- **math** — pour calculer les distances euclidiennes

---

## Fonctionnement simplifié

1. Les coordonnées des points sont définies ou générées aléatoirement.
2. Toutes les paires de points sont évaluées pour connaître leur distance.
3. Les connexions sont triées par distance croissante.
4. On ajoute une connexion **seulement si elle ne crée pas de boucle** (grâce à la fonction `est_relié`).
5. Le graphe est tracé au fur et à mesure avec `matplotlib`.

Le programme affiche ensuite la **distance totale minimale** pour relier tous les points.

---

## Points faibles du code (hérités de l’époque)

Ce projet date de mes débuts, il comporte donc plusieurs limites :
- Code **monolithique** sans séparation claire entre logique et affichage.
- Pas de véritable **structure de graphe** ni d’optimisation de la recherche de connexions.
- L’algorithme `est_relié` est **complexe et peu efficace** (temps de calcul exponentiel sur de gros graphes).
- Pas de gestion des erreurs ni de validation des entrées.
- Le programme **affiche chaque étape**, ce qui ralentit considérablement l’exécution pour de grandes valeurs de `n`.

---

## Pistes d’amélioration

Aujourd’hui, je pourrais améliorer ce projet en :
- Utilisant une **structure de graphe** avec des bibliothèques comme `networkx`.
- Remplaçant la logique maison par un **algorithme de Kruskal ou Prim optimisé**.
- Ajoutant une **complexité calculée et affichée** (O(E log V)).
- Offrant une **interface graphique** simple pour modifier les points ou voir le graphe final.
- Rendant le code plus modulaire (séparer calcul / affichage / génération).

---

##  Conclusion

Ce programme a été un excellent **premier contact avec l’algorithmique et la géométrie computationnelle**.  
Il m’a permis de comprendre la logique des graphes, des distances et des algorithmes d’optimisation, bien avant d’apprendre les structures de données plus avancées.

---

*Projet d’apprentissage — écrit au collège pour explorer les algorithmes de graphes et la visualisation Python.*
