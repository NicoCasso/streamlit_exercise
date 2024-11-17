import streamlit as st
from typing import cast

import pages.customfunctions as cf
from pages.pydanticclasses import *
from pages.questionfields import QuestionFields

quiz = cf.load_model(cf.FILENAME)
dict_quiz = quiz.model_dump()
list_questions = dict_quiz[QuestionFields.QUESTIONS]
nb_questions = len(list_questions)
st.title("Quiz, {0} question{1}.".format(nb_questions,"s" if nb_questions>1 else ""))

if st.session_state.get("current_question") == None :
    st.write("  Ajouter une question au formulaire :")
else :
    st.write("  Question actuelle :")

current_question = {}
if st.session_state.get("current_question") == None :
    form_question_text = st.text_area("Enoncé")
    current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
    current_question[QuestionFields.ANSWERS.value] = []
    st.session_state["current_question"] =  current_question
    st.write("Pas de réponse.")
else :
    current_question = st.session_state["current_question"]
    #update question if it has changed :
    form_question_text = st.text_area("Enoncé", current_question[QuestionFields.QUESTIONTEXT.value])
    nb_answers =  len(current_question[QuestionFields.ANSWERS.value])
    if nb_answers == 0 :
        st.write("Pas de réponses.")
    else :
        st.write("Réponses :")

st.session_state["current_question"] = current_question
responses = current_question[QuestionFields.ANSWERS.value]
for response in responses :
    st.write("    - Réponse n°{0} : {1}, is_correct = {2}".format(
        response[QuestionFields.ANSWERID.value], 
        response[QuestionFields.ANSWERTEXT.value],
        response[QuestionFields.ANSWERCORRECT.value]))

current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text

with st.form("answer_form", clear_on_submit=True):
    st.write("Définir une réponse à cette question :")
    form_answer_text = st.text_input("Texte de la réponse")
    form_answer_correct = st.checkbox("Cette réponse est correcte")
    if st.form_submit_button('Ajouter cette réponse') :
        if form_question_text != "" :
            answers = current_question[QuestionFields.ANSWERS.value]
            current_answer = {}
            current_answer[QuestionFields.ANSWERID.value] = cf.get_id(responses, QuestionFields.ANSWERID.value)
            current_answer[QuestionFields.ANSWERTEXT.value] = form_answer_text
            current_answer[QuestionFields.ANSWERCORRECT.value] = form_answer_correct

            cast(list,responses).append(current_answer)
            current_question[QuestionFields.ANSWERS.value] = answers
            st.session_state["current_question"] = current_question
            st.rerun()

st.session_state["current_question"] = current_question

#DEBUG !
st.write(st.session_state)

if st.button('Enregistrer la question') :
    current_question = st.session_state["current_question"] 
    if cf.validate_question_data(current_question) : 
        temp_list = cast(list[dict], list_questions)
        current_question[QuestionFields.QUESTIONID] = cf.get_id(temp_list, QuestionFields.QUESTIONID.value)
        temp_list.append(current_question)

        quiz = Quiz(questions = temp_list)
        cf.save_model(cf.FILENAME, quiz)
        st.session_state.clear()
        form_question_text = ""
        form_response_text = ""
        form_response_correct = ""
        st.rerun()



