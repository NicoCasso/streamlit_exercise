import json as js
from pages.questionfields import QuestionFields

FILENAME = "liste_questions.json"

def load(filename : str) -> dict :

    exist = False
    try:
        with open(filename): pass
        exist = True
    except IOError: pass

    if not exist : 
        with open(filename, mode="x", encoding="utf-8") as  write_file:
            root_text = "{\"" + QuestionFields.QUESTIONS.value + "\": []}"
            write_file.write(root_text)

    liste_questions = {}
    with open(filename, mode="r", encoding="utf-8") as read_file:
        content = read_file.read()
        liste_questions = js.loads(content)

    return liste_questions

def get_id(liste : list[dict], fieldname : str) -> int :
    new_one = 1
    for dic in liste :
        if dic.get(fieldname) == None:
            continue

        if dic[fieldname] >= new_one :
            new_one+=1

    return new_one

def validate_question_data(question_data : dict) :
    if question_data[QuestionFields.QUESTIONTEXT.value] == "" :
        return False    
    
    #question_data["reponse_type"] 
    if question_data[QuestionFields.RESPONSES.value] == "" :
        return False
    
    return True

def save(filename : str, dico : dict):
    with open(filename, mode="w", encoding="utf-8") as  write_file:
        write_file.write(js.dumps(dico, indent=4))
