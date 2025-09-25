# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 14:13:37 2025

@author: Mathias
"""



def ajouter_noeud(graphe, noeud):
    """
    graphe: graphe a modifier
    noeud: noeud a ajouter
    """

    if (noeud in graphe) == 0 : 
        graphe[noeud] = []

def ajouter_arete(graphe, noeud, arete):
    """
    graphe: graphe a modifier
    noeud: noeud auquel nous allons ajouter l'arete
    arete: arete que nous allons ajouter
    """
    if noeud in graphe:
        if (arete in graphe[noeud]) == 0:
            graphe[noeud].append(arete)
                
                
                