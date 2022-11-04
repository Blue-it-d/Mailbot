text ="""
Moin bot, 
Bitte lege den Arbeitsvertrag mit folgenden Informationen an:
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

import spacy

def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

#
# nlp = spacy.load("de_core_news_sm")

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey", "hallo", "guten tag", "guten morgen", "guten abend", "guten nacht", "Moin")

# genreating essential keys nlp 
def generate_keys(text):
    #split text in lines and remove empty
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
        print(d, d.pos_, d.lemma_)


generate_keys(text)