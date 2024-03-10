from data import quiz_questions
from question_data import Questions
from quiz_brain import QuizBrain
import os

old_score = 0
try_again = True
while try_again:
    questions = []

    for item in quiz_questions:
        question_text = item["question"]
        question_choice = item["options"]
        question_answer = item["answer"]
        new_question = Questions(question_text, question_choice, question_answer)
        questions.append(new_question)

    quiz = QuizBrain(questions)

    while quiz.has_questions():
        print(quiz.next_question())
        os.system('cls')

    if old_score == 0:
        print(f"You've completed the quiz. your final score is: {quiz.score}/{quiz.question_number}")
    else:
        scale = quiz.score - old_score
        if scale > 0:
            print(f"Your new score is better by : +{scale}")
        elif scale < 0:
            print(f"Your new score is worse by: {scale}")
        elif scale == 0:
            print(f"Your new score is the same as your old score.")

    again = input("Do you want to try again. (yes/no): ").lower()

    if again == "yes" or again == "y":
        old_score = quiz.score
    else:
        try_again = False

input("Tap Enter to Exit!")
