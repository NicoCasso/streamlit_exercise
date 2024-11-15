import streamlit as st
import pages.customfunctions as cf
from pages.questionfields import QuestionFields

liste_questions = cf.load(cf.FILENAME)
questions = liste_questions[QuestionFields.QUESTIONS]

no_question = 1
if st.session_state.get("no_question") != None :
    no_question = st.session_state["no_question"]

st.title(f"Le quiz lui même, question n°{no_question}/{len(questions)}")

current_question = questions[no_question-1]

#with st.form("Formulaire_reponse"):
st.write(f"question n°{no_question}")
st.text(current_question[QuestionFields.QUESTIONTEXT])
#st.write(f"réponse attendue sous forme de {current_question["response_text"]}" )

answers = list(map(lambda answer : answer[QuestionFields.RESPONSETEXT], current_question[QuestionFields.RESPONSES]))

form_radio_answer = st.radio("Votre réponse : ", answers)
st.write(form_radio_answer)

   # if st.form_submit_button('Comptabiliser cette réponse') :
if st.button('Comptabiliser cette réponse') :
    next = no_question + 1 
    if next < len(questions) :
        st.session_state["no_question"] = no_question + 1
    else : 
        st.session_state.clear()

    st.rerun()
        
        
