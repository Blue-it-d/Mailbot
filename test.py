#https://blog.ouseful.info/2022/09/30/creating-rule-based-entity-pattern-matchers-in-spacy/

# a Texte preprocessing is needed to remove the punctuation and the stop words, lemmatize the words,
# remove the words that are not verbs and nouns.

import spacy
# Define paterns for adding user in german language


nlp = spacy.load('de_core_news_sm')
ruler = nlp.add_pipe("entity_ruler")

patterns = [
            {"label": "ADD", "pattern": [{"TEXT": {"REGEX": "(legen|anlegen|erstellen|hinzufügen|einfügen|eintragen)"}}]}
            {"label": "USER", "pattern":[{"TEXT": {"REGX"}: "(nutzer|user|hilfskraft|person)"}]},
            {"label": "FACHBEREICH", "pattern":[{"TEXT": {"REGX"}: "(fachbereich|arbeitsgruppe|fach)"}] },
            {"label": "CONTRACT", "pattern":[{"TEXT": {"REGX"}: "(arbeitsvertrag|Hilfskraftarbeitsvertrag)"}]},
            ]

ruler.add_patterns(patterns)           
doc = nlp("TSome Text to be matched")
print([(ent.text, ent.label_) for ent in doc.ents])