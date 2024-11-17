import streamlit as st
import pandas as pd
import numpy as np

import pages.customfunctions as cf
from pages.pydanticclasses import *
from pages.questionfields import QuestionFields

quiz = cf.load_model(cf.FILENAME)
dict_quiz = quiz.model_dump()
dict_questions = dict_quiz[QuestionFields.QUESTIONS]

no_question = 1
if st.session_state.get("no_question") != None :
    no_question = st.session_state["no_question"]

if no_question == len(dict_questions):
    st.title("Résultat du quiz")
    answers = {}
    no_question = 1
    question_count =0
    answer_count = 0 
    for question in dict_questions :
        question_count+=1
        answer_key = "question{0}".format(question[QuestionFields.QUESTIONID])
        if st.session_state.get(answer_key) != None :
             validated =  st.session_state[answer_key]
             if validated : 
                 answer_count+=1

             st.write("{0} : {1}".format(answer_key, validated))

        # if value: 
        #     count += 1
        #     for answer in question[QuestionFields.RESPONSES] :
        #         validated = False
        #         if answer[QuestionFields.RESPONSEID] == st.session_state[answer_key] :
        #             validated = True
                
        #         answers["Question {0}".format(no_question)] = validated

    # table_data = {}
    # table_data["Question number"] = []
    # table_data["Answer"] = []
    # count = 0
    # for num, validated in answers.items() :
    #     numbers = table_data["Question number"]
    #     vals = table_data["Answer"]
    #     numbers.append(num)
    #     vals.append(validated)
    #     table_data["Question number"] = numbers
    #     table_data["Answer"] = vals
    #     if validated : 
    #         count +=1

    # df = pd.DataFrame(data = table_data )
    # st.table(df)

    # st.write("Score : {0}/{1}".format(count, len(table_data["Answer"])))

    
    st.write("Score : {0}/{1}".format(answer_count, question_count))

    if st.button("Recommencer") :
        st.session_state.clear()
        st.rerun()

else :

    st.title(f"Le quiz lui même, question n°{no_question}/{len(dict_questions)}")

    st.write(st.session_state)

    current_question = dict_questions[no_question-1]

    #with st.form("Formulaire_reponse"):
    st.write(f"question n°{no_question}")
    st.text(current_question[QuestionFields.QUESTIONTEXT])
    #st.write(f"réponse attendue sous forme de {current_question["response_text"]}" )

    answers = list(map(lambda answer : answer[QuestionFields.ANSWERTEXT], current_question[QuestionFields.ANSWERS]))

    form_radio_answer = st.radio("Votre réponse : ", answers)
    st.write(form_radio_answer)

    # if st.form_submit_button('Comptabiliser cette réponse') :
    if st.button('Comptabiliser cette réponse') :

        answer_key = "" 
        answer_id = -1
        for answer in current_question[QuestionFields.ANSWERS] :
            if answer[QuestionFields.ANSWERTEXT] == form_radio_answer :
                answer_id = answer[QuestionFields.ANSWERID]
                answer_key = "question{0}".format(current_question[QuestionFields.QUESTIONID])
                break

        if answer_key != "":
            st.session_state[answer_key] = answer_id

        next = no_question + 1 
        if next < len(dict_questions) + 1 :
            st.session_state["no_question"] = no_question + 1

        st.rerun()
            
            
