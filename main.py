from data import quiz_questions  # Importing the quiz questions
from question_data import Questions  # Importing the Questions class
from quiz_brain import QuizBrain  # Importing the QuizBrain class
import os

old_score = 0  # Initializing the old score to 0
try_again = True

while try_again:
    questions = []

    # Creating Question objects from the quiz_questions data
    for item in quiz_questions:
        question_text = item["question"]
        question_choice = item["options"]
        question_answer = item["answer"]
        new_question = Questions(question_text, question_choice, question_answer)
        questions.append(new_question)

    quiz = QuizBrain(questions)  # Creating a QuizBrain object

    # Looping through the quiz questions
    while quiz.has_questions():
        print(quiz.next_question())  # Displaying the next question
        os.system('cls')  # Clearing the console screen

    # Providing feedback on the user's performance
    if old_score == 0:
        print(f"You've completed the quiz. Your final score is: {quiz.score}/{quiz.question_number}")
    else:
        scale = quiz.score - old_score
        if scale > 0:
            print(f"Your new score is better by: +{scale}")
        elif scale < 0:
            print(f"Your new score is worse by: {scale}")
        elif scale == 0:
            print(f"Your new score is the same as your old score.")

    # Asking the user if they want to try again
    again = input("Do you want to try again? (yes/no): ").lower()

    if again == "yes" or again == "y":
        old_score = quiz.score  # Updating the old score
    else:
        try_again = False  # Exiting the loop if the user doesn't want to try again

# Waiting for user input before exiting
input("Tap Enter to Exit!")
