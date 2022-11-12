"""
Dateset patterns for the mathcer
"""
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",
                   "hallo", "guten tag", "guten morgen", "guten abend", "guten nacht", "moin", "servus")

ADD_PATTERN = {"label": "ADD", "pattern": [{"LEMMA": {"IN": ["legen", "eintragen",
                                            "anlegen", "erstellen", "hinzufügen"]}},
                                           ]}


USER_PATTERN = {"label": "USER", "pattern": [{"LOWER": {"IN": ["user", "mitarbeiter",
                                                               "mitarbeiterin", "angestellter", "angestellte",
                                                               "benutzer", "nutzer", "nutzerin", "person"
                                                               ]}}]}

CONTRACT_PATTERN = {"label": "CONTRACT", "pattern": [
            {"LOWER": {"IN": ["vertrag", "arbeitsvertrag", "vertragsverhältnis"]}}]}

DEPARTMENT_PATTERN = {"label": "DEP", "pattern": [
            {"LOWER": {"IN": ["fachbereich", "arbeitsgruppe"]}}]}
