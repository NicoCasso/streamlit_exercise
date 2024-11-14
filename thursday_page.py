import streamlit as st

#streamlit run thursday_page.py

creation_page = st.Page("pages/quiz_creation_page.py")
#creation_page.title = "Création de quizz"

interactive_page = st.Page("pages/interactive_quiz_page.py")
#interactive_page.title = "Lancer le questionnaire"

pages = []
pages.append(creation_page)
pages.append(interactive_page)

pg = st.navigation(pages)
#pg.title = "Page principale"
pg.run()