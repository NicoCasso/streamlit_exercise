from enum import StrEnum

class QuestionFields(StrEnum):
    QUESTIONS = "questions"
    QUESTIONID = "question_id"
    QUESTIONTEXT = "question_text"
    ANSWERS = "answers"
    ANSWERID = "answer_id"
    ANSWERTEXT = "answer_text"
    ANSWERCORRECT = "is_correct"