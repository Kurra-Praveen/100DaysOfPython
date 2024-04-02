from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questionBank = []
for question in question_data:
    qText = question["question"]
    qAnswer = question["correct_answer"]
    myQuestion = Question(qText, qAnswer)
    questionBank.append(myQuestion)

quiz = QuizBrain(questionBank)
score = 0
while quiz.stillHasQuestion():
    if quiz.nextQuestion():
        score += 1
        print(f"your current score is {score}")
    else:
        print(f" Game Over! your score is  {score}")
        break
