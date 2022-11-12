#from controlweb.jobs import add_user, add_department, add_contract

import os

import spacy
from patterns import GREETING_INPUTS

TEXT = """
Moin bot, 
ich muss einen Nutzer mit folgenden Informationen hinzufügen:
Vorname: Mustermann, Nachname: Müller, geb. am: 04.04.1991, Anschrift:
BeispielStraße 11 49074 Osnabrück, Arbeitsstunden: 30, Startdatum: 1-1-
2023, Enddatum: 31-12-2021, Arbeitsgruppe: Softwareengeniering Projekt-
bezeichnung: HSP Urlaubsstunden: 20, Überstunden aus vorherigem Vertrag:
10
Danke.
"""

def save_to_file(text) -> None:
    """Save given text to a file."""
    with open("tmp.txt", "w", encoding="utf-8") as file:
        file.write(text)

def delete_file(name="tmp.txt"):
    """Delete the file with the given name."""
    os.remove(name)


def text_preprocessing(text):
    """
    - remove greeting and extruct the first line 
    - remove empty lines
    - Split text in smaller segments "Tokens"
    - Labeling the tokens with POS
    - Reduce words into thier roots for better analysis "lemmatization"
    - Filter out fillings and stop words 
    - then generate essential words with only the nouns and verbs with spacy
    - this will apply to the first sentence after the greeting.
    """
    # this is used to save text to a file in case something goes wrong
    save_to_file(text)

    # split text in lines and remove empty
    lines = [line for line in text.splitlines() if line.strip()]

    # check if first line is empty or greeting
    if (word in lines[0].lower for word in GREETING_INPUTS):
        lines.pop(0)

    nlp = spacy.load("de_core_news_sm")
    # split text in tokens for the first line afret the greeting
    doc = nlp(lines[0])

    key_list = []
    # Extracting the essential words (verbs and nouns)
    for token in doc:
        if token.pos_ in ["NOUN", "VERB"]:
            # save the lemmatized word
            key_list.append(token.lemma_)

    delete_file()
    return key_list


print(text_preprocessing(text))


def check(text):
    nlp = spacy.load('de_core_news_sm')
    ruler = nlp.add_pipe("entity_ruler")
    """ {"label": "ADD", "pattern": [{"LEMMA": {"IN": ["legen", "eintragen" ,"anlegen", "erstellen", "hinzufügen"]}},
                                     {"POS": "NOUN"}]},
         """
    patterns = [
        {"label": "ADD", "pattern": [{"LEMMA": {"IN": ["legen", "eintragen", "anlegen", "erstellen", "hinzufügen"]}},
                                     ]},
        {"label": "USER", "pattern": [{"LOWER": {"IN": ["user", "mitarbeiter", "mitarbeiterin", "angestellter", "angestellte",
                                                        "benutzer", "nutzer", "Nutzerin", "person"
                                                        ]}}]},
        {"label": "CONTRACT", "pattern": [
            {"LOWER": {"IN": ["vertrag", "arbeitsvertrag", "vertragsverhältnis"]}}]},
        {"label": "DEP", "pattern": [
            {"LOWER": {"IN": ["fachbereich", "arbeitsgruppe"]}}]}
    ]
    ruler.add_patterns(patterns)
    doc = nlp(text)
    print(doc[0].lemma_)
    print("doc", doc.ents)
    print([(ent.text, ent.label_) for ent in doc.ents])


""" x = tex_preproccessing(text)
# rejoin the return list to a string
print(x)
x = " ".join(x)
print(x)
check(x)
 """
