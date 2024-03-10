class QuizBrain:
    def __init__(self, question_list):
        """
        Initializes a QuizBrain object with a list of questions.

        Args:
        question_list (list): List of Questions objects.
        """
        self.question_number = 0   # Current question number
        self.question_list = question_list   # List of Questions objects
        self.score = 0   # Current score

    def next_question(self):
        """
        Displays the next question from the list and prompts the user for an answer.
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q{self.question_number}: {current_question.question}\n"  # Displaying the question text and options
                            f"{current_question.options[0]}\n"
                            f"{current_question.options[1]}\n"
                            f"{current_question.options[2]}\n"
                            f"{current_question.options[3]}\n"
                            f"Your choice: ")
        self.check_answer(user_choice, current_question.answer)

    def has_questions(self):
        """
        Checks if there are still questions left in the question list.

        Returns:
        bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_choice, correct_answer):
        """
        Checks if the user's choice matches the correct answer.

        Args:
        user_choice (str): The user's choice.
        correct_answer (str): The correct answer to the current question.
        """
        if user_choice.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer is: {correct_answer}")

        # Display the current score
        print(f"Your current score is: {self.score}/{self.question_number}")
        input("Tap Enter to Continue!")
