import streamlit as st

from typing import cast

import pages.customfunctions as cf
from pages.questionfields import QuestionFields

liste_questions = cf.load(cf.FILENAME)

st.write("Création de quizz")

questions = liste_questions[QuestionFields.ROOT.value]
st.write(f"    Nombre de questions {len(questions)}")

with st.form("Formulaire_question", True):
   st.write("ajouter une question au formulaire")
   #my_number = st.slider('Pick a number', 1, 10)
   #my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   form_question_text = st.text_input("Texte de la question")
   form_response_type = st.selectbox('Type de réponse attendue', ['texte','entier','réel','vrai ou faux'])
   form_response_text = st.text_input("réponse provisoire")

   st.form_submit_button('Enregistrer')

# This is outside the form

st.write(st.session_state)

if st.session_state["FormSubmitter:Formulaire_question-Enregistrer"] == True :
    temp_list = cast(list[dict],liste_questions[QuestionFields.ROOT.value])

    current_question = {}
    current_question[QuestionFields.QUESTIONTEXT.value] = form_question_text
    current_question[QuestionFields.RESPONSETYPE.value] = form_response_type
    current_question[QuestionFields.RESPONSETEXT.value] = form_response_text

    st.form

    if cf.validate_question_data(current_question) :
        current_question[QuestionFields.QUESTIONID] = cf.get_id(temp_list, QuestionFields.QUESTIONID.value)
        temp_list.append(current_question)
        liste_questions[QuestionFields.ROOT.value] = temp_list

        st.write(f"nouvel id : {current_question[QuestionFields.QUESTIONID.value]}")
        st.write(form_question_text)
        st.write(form_response_type)
        st.write(form_response_text)

        cf.save(cf.FILENAME, liste_questions)



