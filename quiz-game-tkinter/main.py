from question_data import QuestionData
from quiz_brain import QuizBrain
from quiz_ui import QuizUI

question_bank = QuestionData(10)
quiz_brain = QuizBrain(question_bank.question_list)
ui = QuizUI(quiz_brain)
