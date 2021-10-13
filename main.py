from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests

API_URL = "https://opentdb.com/api.php"
API_PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}

# ------------ GET QUESTION DATA FROM OPEN TRIVIA DB ------------ #
response = requests.get(url=API_URL, params=API_PARAMETERS)
response.raise_for_status()
question_data = response.json()["results"]


# ------------------ CREATE QUESTION BANK ----------------------- #
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# ------------------ CREATE AND RUN QUIZ ------------------------ #
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

# ------------------- END OF PROGRAM ---------------------------- #
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
