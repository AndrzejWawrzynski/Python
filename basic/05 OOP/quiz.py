import requests
import html
from deep_translator import GoogleTranslator


class Question:
    def __init__(self, category, questionStr, correctAnswerFlag) -> None:
        self.category = category
        questionStr = GoogleTranslator(source='auto', target=language).translate(questionStr)
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag

class Quiz:
    def __init__(self, numQuestion):
        self.apiUrl = "https://opentdb.com/api.php?difficulty="+d+"&type=boolean&amount="
        self.numquestion = numQuestion
        self.questionList = []
        self.loadQuestions(numQuestion)

    def loadQuestions(self, numQuestion):
        response = requests.get(self.apiUrl + str(numQuestion))
        # {'response_code': 0, 'results': [{'type': 'boolean', 'difficulty': 
        # 'easy', 'category': 'General Knowledge', 'question': 
        # 'Bulls are attracted to the color red.', 'correct_answer': 
        # 'False', 'incorrect_answers': ['True']}]}
        if response.ok:
            # print(response.json())
            data = response.json()
            results = data["results"]

            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape (q["question"])
                correctAnswerFlag = q["correct_answer"].lower() in ["true", "1", "yes"]
                #print(q["correct_answer"], correctAnswerFlag)
                # incorrectAnswers = q["incorrect_answers"]
                # print(question)
                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionList.append(qObj)
                  

    def stratQuiz(self):
        print("\nWelcome in Quiz!")
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questionList)

        while (n < numQuestions):
            q = self.questionList[n]
            print("Question number " + str(n+1) + " :" , q.questionStr)
            #print("Answer Flag: ", q.correctAnswerFlag)
            anwer = input("Give correct answer as y/n:")
            answerBool = False
            if anwer =="y": answerBool = True
            
            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")
            n +=1
        
        print("Number of correct aswers: ", numCorrectUserAnswers, 
              " from ", len(self.questionList), " questions")

d = "easy"
language = "pl"
quiz = Quiz(10)
quiz.stratQuiz()
