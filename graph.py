# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 14:13:37 2025

@author: Mathias
"""



def ajouter_noeud(graphe, noeud):
    if (noeud in graphe) == 0 : 
        graphe[noeud] = []

def ajouter_arete(graphe, noeud, arete):
    if noeud in graphe:
        if (arete in graphe[noeud]) == 0:
            graphe[noeud].append(arete)
                
                
                