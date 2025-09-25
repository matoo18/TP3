# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 13:56:57 2025

@author: Mathias
"""

from utils import *
from graph import *

graphe = { "A":["B"], "B":[], "C":["A","B"], "D":["C"], "E":["C","D"]}

display_graph_from_dict(graphe)

ajouter_noeud(graphe, "X")
ajouter_arete(graphe, "X", "E")

display_graph_from_dict(graphe)