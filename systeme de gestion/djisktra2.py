import numpy as np
import math

def dijkstraDist(G, depart):
    N = np.size(G, 0)
    pcc = {}  # Utilisation d'un dictionnaire pour stocker les informations sur les sommets
    for i in range(N):
        pcc[i] = {'distance': math.inf, 'visite': False, 'precedent': None}  # Initialisation des sommets
    sommet_u = depart
    dist_u = 0
    pcc[depart]['distance'] = 0
    pcc[depart]['visite'] = True
    cpt = 0
    while cpt != N - 1:
        minimum = math.inf
        for k in range(N):
            if not pcc[k]['visite']:
                dist_uv = G[sommet_u][k]
                dist_totale = dist_u + dist_uv
                if dist_totale < pcc[k]['distance']:
                    pcc[k]['distance'] = dist_totale
                    pcc[k]['precedent'] = sommet_u
                if pcc[k]['distance'] < minimum:
                    minimum = pcc[k]['distance']
                    prochain_sommet_select = k
        cpt += 1
        sommet_u = prochain_sommet_select
        pcc[sommet_u]['visite'] = True
        dist_u = pcc[sommet_u]['distance']
    return pcc

def dijkstraPCC(G, depart, arrivee):
    pcc = dijkstraDist(G, depart)
    chemin = []
    ville = arrivee
    chemin.append(ville)
    while ville != depart:
        ville = pcc[ville]['precedent']
        chemin.append(ville)
    return list(reversed(chemin))

# Graphe
G = np.array([[math.inf, 1, 4, math.inf],
              [math.inf, math.inf, 2, 5],
              [math.inf, math.inf, math.inf, 1],
              [math.inf, math.inf, math.inf, math.inf]])

depart = 0
arrivee = 2

resultat_dijkstra_dist = dijkstraDist(G, depart)
resultat_dijkstra_pcc = dijkstraPCC(G, depart, arrivee)

print("Résultat de Dijkstra (Distances) :", resultat_dijkstra_dist)
print("Plus court chemin de", depart, "à", arrivee, ":", resultat_dijkstra_pcc)
