"""
Titre : Arbre couvrant de poids minimal
"""
import math, itertools
import numpy as np
import matplotlib.pyplot as plt
import random

#Partie pas demandée dans l'énoncé, mais utile pour avoir un visuel de ce qu'il se passe
def visuel(points, connections):
    """
    La fonction prend en entrée les points ainsi que les connections entre les points
    et réalise un graphique en reliant ces points
    """
    points = np.array(points) # On convertit la liste des coordonnées des points en tableau numpy
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y, color='blue') #On affiche les points
    for connection in connections: #On fait les connections en rouge
        x = [points[i][0] for i in connection]
        y = [points[i][1] for i in connection]
        plt.plot(x, y, color='red', marker='o')
    for i, point in enumerate(points): #annotation des points
        plt.annotate(str(i), (point[0], point[1]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Représentation des lignes')
    plt.grid(True)
    plt.show()

#---PROGRAMME---

def distance(co1, co2):
    """
    Utilise le théorème de pythagore afin de calculer la distance entre deux point
    à partir de leurs coordonnées. 
    """
    return math.sqrt((co1[0] - co2[0])**2+(co1[1] - co2[1])**2)

def réseau_proche(connections, number):
    """
    Cette fonction permet de trouver dans quelles connection (tuple) se situe un point (number)
    elle renvoie les connections
    """
    if number in [e for connect in connections for e in connect]:
        connectics = []
        for element in connections:
            if number in element:
                connectics.append(element[element.index(number)-1])
        return(connectics)

def est_relié(connections, number, target):
    """
    Cette fonction utilise -réseau proche- (fonction précédente) pour obtenir les réseaux proches
    des réseaux proches des points, et ainsi permet de savoir si un point est relié à un autre
    même si il est pas directement relié.
    """
    if connections == [] or not number in [e for connect in connections for e in connect]:
        return False
    number = [number]
    old = []
    i = 0
    while old != number and not target in number:
        old = number if i%2 == 0 else old #permet à old d'obtenir l'ancienne valeur (évite la boucle infinie)
        c = []
        for e in number:
            c.append(réseau_proche(connections, e))
        c = list(set([e for b in c for e in b])) #efface les doublons
        number = c
        i += 1
    print(i)
   
    return(target in number)

def distance_minimale(n, coos):
    """
    Calcule la distance minimale de fil pour relier tous les points
    """
    combis = list(itertools.combinations(range(n), 2)) #créer toutes les combinaisons de liens
    d = []
    for combi in combis: 
        d.append(((combi), distance(coos[combi[0]], coos[combi[1]]))) #créer la liste de toutes les distances de toutes les combinaisons de liens
    d.sort(key = lambda x: x[1]) #Trier cette liste dans l'ordre croissant des distances (key = lambda x: x[1]) car liste de tuples avec les distances en deuxième position de chaque tuple
    chemins = [] #liste des chemins créés
    comp = 0
    plt.ion()  # Activation du mode interactif
    while comp < n-1: #le total de chemins doit être de n-1
        connections = [element[0] for element in chemins] #toutes les connections 
        if not est_relié(connections, d[comp][0][0], d[comp][0][1]): #On vérifie la connection n'est pas déjà faite indirectement
            chemins.append(d[comp]) #On ajoute la connection dans les chemins
            plt.draw()
            visuel(coos, [element[0] for element in chemins])
            #plt.pause(.05)  # Pause d'une seconde
        else:
            n += 1 #On ajoute 1 à n pour passer au chemin suivant sans affecter la boucle
        comp += 1
    plt.ioff()  # Désactivation du mode interactif
    total = 0 #calcul du total
    for i in range(len(chemins)):
        total += chemins[i][1]
    #Visuel des chemmins et connections
    return int(total)

#---les entrées---
n = 4
coos = [(-1664,-2941), (1969,-4009),(7953, -5787),(-1136,-1206)]
print("La distance minimale est :",distance_minimale(n, coos))
plt.clf()
n = 13
coos = [(-2291, -71), (-2784, -9693), (-8879,4618),(986, -8203),(-4634,-1894),(8827,-5805),(7918,-2780),(5618,-690),(-7167,2618),(437,-9308),(-5573,9370),(-3072,-3439),(6832,-5064)]
print("La distance minimale est :",distance_minimale(n, coos))
plt.clf()

n = 2
for i in range(10):
    n = n*2
    coos = [(random.randint(-9000, 9000), random.randint(-9000, 9000)) for i in range(n)]
    print("La distance minimale est :",distance_minimale(n, coos))
    plt.pause(3)
    plt.clf()