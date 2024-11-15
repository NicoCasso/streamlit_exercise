import streamlit as st
from typing import cast

import pages.customfunctions as cf
from pages.questionfields import QuestionFields
from pages.fieldtype import FieldType

liste_questions = cf.load(cf.FILENAME)
questions = liste_questions[QuestionFields.QUESTIONS.value]
nb_questions = len(questions)
st.title(f"Quiz, {nb_questions} question{"s" if nb_questions>1 else "" }.")

if st.session_state.get("current_question") == None :
    st.write("  Ajouter une question au formulaire :")
else :
    st.write("  Question actuelle :")



current_question = {}
if st.session_state.get("current_question") == None :
    form_question_text = st.text_area("Enoncé")
    current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
    current_question[QuestionFields.RESPONSES.value] = []
    st.session_state["current_question"] =  current_question
    st.write("Pas de réponse.")
else :
    current_question = st.session_state["current_question"]
    #update question if it has changed :
    form_question_text = st.text_area("Enoncé", current_question[QuestionFields.QUESTIONTEXT.value])
    nb_responses =  len(current_question[QuestionFields.RESPONSES.value])
    if nb_responses == 0 :
        st.write("Pas de réponses.")
    else :
        st.write("Réponses :")

st.session_state["current_question"] = current_question
responses = current_question[QuestionFields.RESPONSES.value]
for response in responses :
    st.write("    - Réponse n°{0} : {1}, is_correct = {2}".format(
        response[QuestionFields.RESPONSEID.value], 
        response[QuestionFields.RESPONSETEXT.value],
        response[QuestionFields.RESPONSECORRECT.value]))

current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text

with st.form("response_form", clear_on_submit=True):
    st.write("Définir une réponse à cette question :")
    form_response_text = st.text_input("Texte de la réponse")
    form_response_correct = st.checkbox("Cette réponse est correcte")
    if st.form_submit_button('Ajouter cette réponse') :
        if form_question_text != "" :
            responses = current_question[QuestionFields.RESPONSES.value]
            current_response = {}
            current_response[QuestionFields.RESPONSEID.value] = cf.get_id(responses, QuestionFields.RESPONSEID.value)
            current_response[QuestionFields.RESPONSETEXT.value] = form_response_text
            current_response[QuestionFields.RESPONSECORRECT.value] = form_response_correct

            cast(list,responses).append(current_response)
            current_question[QuestionFields.RESPONSES.value] = responses
            st.session_state["current_question"] = current_question

st.session_state["current_question"] = current_question

#DEBUG !
st.write(st.session_state)

if st.button('Enregistrer la question') :
    current_question = st.session_state["current_question"] 
    if cf.validate_question_data(current_question) :
        temp_list = cast(list[dict],liste_questions[QuestionFields.QUESTIONS.value])
        current_question[QuestionFields.QUESTIONID] = cf.get_id(temp_list, QuestionFields.QUESTIONID.value)
        temp_list.append(current_question)
        liste_questions[QuestionFields.QUESTIONS.value] = temp_list

        cf.save(cf.FILENAME, liste_questions)
        st.session_state.clear()
        form_question_text = ""
        form_response_text = ""
        form_response_correct = ""
        st.rerun()



