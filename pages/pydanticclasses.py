from pydantic import BaseModel

class UserAnswer(BaseModel) :
    question_id : int
    question_text : str
    answer_text : str
    is_correct : bool

class UserSession(BaseModel) :
    answers : list[UserAnswer]

class Answer(BaseModel):
    answer_id : int
    answer_text : str
    is_correct : bool

class Question(BaseModel) :
    question_id : int
    question_text : str
    answers : list[Answer]

class Quiz(BaseModel) :
    questions : list[Question]
    