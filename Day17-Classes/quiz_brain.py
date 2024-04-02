import html


def checkAnswer(answer, currentAnswer):
    return answer == currentAnswer


class QuizBrain:

    def __init__(self, questionList):
        self.currentQuestion = None
        self.questionNo = 0
        self.questionList = questionList

    def stillHasQuestion(self):
        return self.questionNo < len(self.questionList)

    def nextQuestion(self):
        self.currentQuestion = self.questionList[self.questionNo]
        self.questionNo += 1
        q_text = html.unescape(self.currentQuestion.text)
        answer = input(f" Q.{self.questionNo}:{q_text} ? (True/False)\n").title()
        return checkAnswer(answer, self.currentQuestion.answer)
