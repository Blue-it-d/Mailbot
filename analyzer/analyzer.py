import spacy
text = """
Moin bot, 
ich moechte einen Fachbereich mit folgenden Informationen eintragen:
Vorname: Mustermann, Nachname: Müller, geb. am: 04.04.1991, Anschrift:
BeispielStraße 11 49074 Osnabrück, Arbeitsstunden: 30, Startdatum: 1-1-
2023, Enddatum: 31-12-2021, Arbeitsgruppe: Softwareengeniering Projekt-
bezeichnung: HSP Urlaubsstunden: 20, Überstunden aus vorherigem Vertrag:
10
Danke.
"""
x = text.splitlines()
""" print(text.splitlines())
print(list(filter(None, x)))
 """


def extract_phone_numbers(string):
    r = re.compile(
        r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]


def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

#
# nlp = spacy.load("de_core_news_sm")


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",
                   "hallo", "guten tag", "guten morgen", "guten abend", "guten nacht", "Moin")

# genreating essential keys nlp


def generate_keys(text):
    # split text in lines and remove empty
    lines = [line for line in text.splitlines() if line.strip()]
    # check if first line is empty or greeting
    if (word in lines[0].lower for word in GREETING_INPUTS):
        lines.pop(0)

    """ 
       for greeting in GREETING_INPUTS:
        if greeting in lines[0].lower():
            lines.pop(0)
            break
     """

    # tokenize the
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(lines[0])

    key_list = []

    for d in doc:
        #print(d, d.pos_, d.lemma_, d.dep_, d.head, d.head.pos_)
        # add to key list if it is a noun or a verb
        if (d.pos_ == "NOUN") or (d.pos_ == "VERB"):
            key_list.append(d.lemma_)
    return key_list

# print(generate_keys(text))

# function to add user


def add_user():
    print("add user")


def add_contract():
    print("add contract")


def add_project():
    print("add project")


""" ess_words = generate_keys(text)
#print(ess_words)
add_user_pattern = [["Arbeitsvertrag", "legen"], ["Arbeitsvertrag", "anlegen"], 
                    ["Arbeitsvertrag", "erstellen"], ["Arbeitsvertrag", "hinyufügen"]],

 """


def text_processing(text):
    """
    remove greeting and extruct the first line 
    then generate essential words with only the nouns and verbs with spacy
    """
    # split text in lines and remove empty
    lines = [line for line in text.splitlines() if line.strip()]
    # check if first line is empty or greeting
    if (word in lines[0].lower for word in GREETING_INPUTS):
        lines.pop(0)

    # tokenize the
    nlp = spacy.load("de_core_news_sm")
    doc = nlp(lines[0])

    key_list = []

    for d in doc:
        #print(d, d.pos_, d.lemma_, d.dep_, d.head, d.head.pos_)
        # add to key list if it is a noun or a verb
        if (d.pos_ == "NOUN") or (d.pos_ == "VERB"):
            key_list.append(d.lemma_)
    return key_list


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


x = text_processing(text)
# rejoin the return list to a string
print(x)
x = " ".join(x)
print(x)
check(x)
