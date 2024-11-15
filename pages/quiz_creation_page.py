import streamlit as st

from typing import cast

import pages.customfunctions as cf
from pages.questionfields import QuestionFields
from pages.fieldtype import FieldType
from pages.statemanager import StateManager

liste_questions = cf.load(cf.FILENAME)
state_manager = StateManager()

st.write("Création de quizz")

questions = liste_questions[QuestionFields.QUESTIONS.value]
st.write(f"    Nombre de questions {len(questions)}")

if st.session_state.get("current_question") == None :
    st.write("ajouter une question au formulaire :")
else :
    st.write("Question actuelle :")

form_question_text = st.text_area("Enoncé")

current_question = {}
if st.session_state.get("current_question") == None :
    current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
    current_question[QuestionFields.RESPONSES.value] = []
    st.session_state["current_question"] =  current_question
    st.write("Pas de réponses.")
else :
    current_question = st.session_state["current_question"]
    #update question if it has changed :
    current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
    nb_responses =  len(current_question[QuestionFields.RESPONSES.value])
    if nb_responses ==0 :
        st.write("Pas de réponses.")
    else :
        st.write("Réponses :")

st.session_state["current_question"] = current_question
responses = current_question[QuestionFields.RESPONSES.value]
for response in responses :
    st.write("    - Réponse n°{0}: {1}, is_correct{2}".format(
        response[QuestionFields.RESPONSEID.value], 
        response[QuestionFields.RESPONSETEXT.value],
        response[QuestionFields.RESPONSECORRECT.value]))

# if form_response_type == FieldType.MULTIPLE.value:

current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
# current_question[QuestionFields.RESPONSETYPE.value] = form_response_type

st.write("ajouter une réponse à la question")
form_question_text = st.text_input("Texte de la réponse")
form_response_correct = st.checkbox("réponse correcte")
if st.button('Ajouter') and form_question_text != "" :
    responses = current_question[QuestionFields.RESPONSES.value]
    current_response = {}
    current_response[QuestionFields.RESPONSEID.value] = cf.get_id(responses, QuestionFields.RESPONSEID.value)
    current_response[QuestionFields.RESPONSETEXT.value] = form_question_text
    current_response[QuestionFields.RESPONSECORRECT.value] = form_response_correct
    cast(list,responses).append(current_response)
    current_question[QuestionFields.RESPONSES.value] = responses
    st.session_state["current_question"] = current_question
    form_question_text = ""
    form_response_correct = False

st.session_state["current_question"] = current_question

st.write(st.session_state)

if st.button('Enregistrer la question') :
    st.write("Enregistrement de :")
    st.write(st.session_state["current_question"])

# if st.session_state["FormSubmitter:Formulaire_response-Enregistrer"] == True :

#     temp_list = cast(list[dict],liste_questions[QuestionFields.QUESTIONS.value])

#     current_question = {}
#     current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
#     current_question[QuestionFields.RESPONSETYPE.value] = form_response_type


#     if cf.validate_question_data(current_question) :
#         current_question[QuestionFields.QUESTIONID] = cf.get_id(temp_list, QuestionFields.QUESTIONID.value)
#         temp_list.append(current_question)
#         liste_questions[QuestionFields.QUESTIONS.value] = temp_list

#         st.write(f"nouvel id : {current_question[QuestionFields.QUESTIONID.value]}")
#         st.write(form_question_text)
#         st.write(form_response_type)

#         cf.save(cf.FILENAME, liste_questions)



