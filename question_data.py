class Questions:
    def __init__(self, question, options, answer):
        """
        Initializes a Questions object with the provided question, options, and answer.

        Args:
        question (str): The text of the question.
        options (list): List of options for the question.
        answer (str): The correct answer to the question.
        """
        self.question = question  # Stores the question text
        self.options = options    # Stores the list of options
        self.answer = answer      # Stores the correct answer
