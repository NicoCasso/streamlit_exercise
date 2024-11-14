from enum import StrEnum

class QuestionFields(StrEnum):
    ROOT = "questions"
    QUESTIONID = "question_id"
    QUESTIONTEXT = "question_text"
    RESPONSETYPE = "response_type"
    RESPONSETEXT = "response_text"