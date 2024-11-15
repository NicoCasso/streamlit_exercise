import streamlit as st
import pages.customfunctions as cf


st.write("interactive quiz page")
liste_questions = cf.load(cf.FILENAME)

st.write("Le quizz lui même")

questions = liste_questions['Questions']
st.write(f"    Nombre de questions {len(questions)}")

no_question = 1
current_question = {}
for question in questions : 
    if question["question_id"] == no_question :
        current_question = question
        break

with st.form("Formulaire_reponse"):
   st.write(f"question n°{no_question}")
   #my_number = st.slider('Pick a number', 1, 10)
   #my_color = st.selectbox('Pick a color', ['red','orange','green','blue','violet'])
   st.write(f"question : {current_question["question_text"]}")
   st.write(f"réponse attendue sous forme de {current_question["response_text"]}" )
   form_response_text = st.text_input("réponse provisoire")

   st.form_submit_button('Enregistrer')