import json as js
from pages.questionfields import QuestionFields
from pages.pydanticclasses import *

FILENAME = "Quiz_questions.json"

def load_model(filename : str) -> Quiz :

    exist = False
    try:
        with open(filename): pass
        exist = True
    except IOError: pass

    rootQuiz = Quiz(questions=[])
    if not exist : 
        with open(filename, mode="x", encoding="utf-8") as  write_file:
            #root_text = "{\"" + QuestionFields.QUESTIONS.value + "\": []}"
            #write_file.write(root_text)
            rootQuiz = Quiz(questions=[])
            write_file.write(rootQuiz.model_dump_json())    

    with open(filename, mode="r", encoding="utf-8") as read_file:
        content = read_file.read()
        #liste_questions = js.loads(content)
        rootQuiz = Quiz.model_validate_json(content)

    return rootQuiz

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
    # if question_data[QuestionFields.RESPONSES.value] == [] :
    #     return False
    
    return True

def save_model(filename : str, quiz : Quiz):
    with open(filename, mode="w", encoding="utf-8") as  write_file:
        write_file.write(quiz.model_dump_json(indent=4))

def save_session(filename : str, session : UserSession):
    with open(filename, mode="w", encoding="utf-8") as  write_file:
        write_file.write(session.model_dump_json(indent=4))