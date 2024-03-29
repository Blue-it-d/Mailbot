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


add_user_token = ("ADD", "USER")
add_rule = {
    "label": add_user_token["ADD"],
    "match_pattern": [
        {"LEMMA": {"REGEX": "(legen|anlegen|erstellen|hinzufügen|einfügen|eintragen)"}},
        # Add better Patterns
    ],
    "weight": 1.0,
    "indispensable": True,
}

user_rule = {
    "label": add_user_token["USER"],
    "match_pattern": [
        {"LEMMA": {"REGEX": "(nutzer|user|hilfskraft|person)"}},],
        # Add better Patterns
        "weight": 1.5,
        "indispensable": True,
    }

# Rule based matcher: add contract
add_contract_token = ("ADD", "CONTRACT")
contract_rule = {
    "label": add_contract_token["CONTRACT"],
    "match_pattern": [
        {"LEMMA": {"REGEX": "(vertrag|arbeitsvertrag|Hilfskraftarbeitsvertrag)"}},],
        # Add better Patterns
        "weight": 1.5,
        "indispensable": True,
    }





"""
NLU that focuses on organizing the
user’s unstructured input such that the chatbot can understand and analyze it.
It contains:
 Syntax analysis: the process of analyzing the structure of a sentence
    - Tokenization
    - Part-of-speech tagging
    - Dependency parsing
    - Lemmatization
    - Named entity recognition
    - Reducing words into their roots for better analysis.
    - Fillter out stop words

Semantic analysis: the process of analyzing the meaning of a sentence
    - distinguishing the context of each word
    - understand the relationships between the words in the text.


NLU models utilize:
    - Supervised machine learning for syntax analysis steps (tokenization, PoS tagging), such as
support vector machines (SVM), Bayesian networks, and maximum entropy algorithms.
    - Unsupervised machine learning for semantic analysis such as clustering algorithms.

 Intent classification:
 Cassifiers are trained on relevant dataset to predict the intent of the user.

 classification utlize:
    - Rules-based pattern matching
    - Machine learning classification algorithms such as decision trees, naive Bayes, and logistic
regression.
    - Deep learning such as artificial neural networks
"""