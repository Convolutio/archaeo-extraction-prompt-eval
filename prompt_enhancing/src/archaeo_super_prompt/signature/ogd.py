from typing import Literal

"""
In most of the case, the sample in the training dataset will have the value
"sito pluristradificato"
"""

ItalianOGD = Literal[
    "area a uso funerario",
    "area di materiale mobile",
    "area priva di tracce archeologiche",
    "elemento toponomastico",
    "giacimento in cavit naturale",
    "giacimento paleontologico",
    "giacimento subacqueo",
    "infrastruttura agraria",
    "infrastruttura assistenziale",
    "infrastruttura di consolidamento",
    "infrastruttura di servizio",
    "infrastruttura idrica",
    "infrastruttura portuale",
    "infrastruttura viaria",
    "insediamento",
    "luogo ad uso pubblico",
    "luogo commemorativo",
    "luogo con deposizione di materiale",
    "luogo con elemento per la confinazione",
    "luogo con ritrovamento sporadico",
    "luogo con tracce di frequentazione",
    "luogo di attivit produttiva",
    "sito non identificato",
    "sito pluristratificato",
    "struttura abitativa",
    "struttura di fortificazione",
    "strutture per il culto",
]
