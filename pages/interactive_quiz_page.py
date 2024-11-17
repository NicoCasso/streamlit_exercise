import streamlit as st
import pandas as pand
import numpy as nump

import pages.customfunctions as cf
from pages.pydanticclasses import *
from pages.questionfields import QuestionFields

quiz = cf.load_model(cf.FILENAME)
dict_quiz = quiz.model_dump()
dict_questions = dict_quiz[QuestionFields.QUESTIONS]

num_question = 1
if st.session_state.get("num_question") != None :
    num_question = st.session_state["num_question"]

if num_question == len(dict_questions) +1 :
    st.title("Résultat du quiz")

    model_answers = []
    for question in dict_questions :
        current_question_id = question[QuestionFields.QUESTIONID.value]
        current_question_text = question[QuestionFields.QUESTIONTEXT.value]
        answer_key = "question{0}".format(current_question_id)
        if st.session_state.get(answer_key) != None :
            answer_id =  st.session_state[answer_key]
            user_answer = {}
            for answer in question[QuestionFields.ANSWERS.value] :
                if answer[QuestionFields.ANSWERID.value] == answer_id :
                    user_answer = answer
                    break
    
            if user_answer !=  {} :
                current_answer_text = user_answer[QuestionFields.ANSWERTEXT.value]
                current_answer_correct = user_answer[QuestionFields.ANSWERCORRECT.value]
            else :
                current_answer_text = "Pas de réponse"
                current_answer_correct = False

            user_answer =  UserAnswer( question_id=current_question_id, 
                question_text = current_question_text, 
                answer_text = current_answer_text, 
                is_correct= current_answer_correct)
            
            model_answers.append(user_answer)
      
    df = pand.DataFrame(data = {
        'question': list(map(lambda x : x.question_text , model_answers)),  
        'réponse': list(map(lambda x : x.answer_text ,model_answers)), 
        'correct' : list(map(lambda x : "VRAI" if x.is_correct else "FAUX" ,model_answers)) } )
    
    st.table(df)

    correct_answers = sum(1 for _ in filter(lambda x: x.is_correct==True, model_answers))
    
    st.write("Score : {0}/{1}".format(correct_answers, len(model_answers)))

    if st.button("Recommencer") :
        st.session_state.clear()
        st.rerun()

else :

    st.title(f"Le quiz lui même, question n°{num_question}/{len(dict_questions)}")

    # DEBUG !
    # st.write(st.session_state)

    current_question = dict_questions[num_question-1]

    st.write(f"question n°{num_question}")
    st.text(current_question[QuestionFields.QUESTIONTEXT])

    answers = list(map(lambda answer : answer[QuestionFields.ANSWERTEXT], current_question[QuestionFields.ANSWERS]))

    form_radio_answer = st.radio("Votre réponse : ", answers)
    st.write(form_radio_answer)

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

        st.session_state["num_question"] = num_question + 1 

        st.rerun()
            
            
