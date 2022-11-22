class QuizBrain:

    def __init__(self, q_list):
        """Initialize a question """
        self.question_number = 0  # default to 0 - index
        self.question_list = q_list  # question list
        self.score = 0  # initial score

        # stopped here

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # TODO: asking the questions
    def next_question(self):
        """Gets a hold of a question """
        current_question = self.question_list[self.question_number]  # filter a question out of question list
        self.question_number += 1  # increase count - generates next question
        user_choice = input(f"Q{self.question_number}. {current_question.text} (True or False)? ")  # user input
        self.check_answer(user_choice, current_question.answer)   # checks user's input with correct answer

    # TODO: checking if answer was correct
    def check_answer(self, user_choice, correct_answer):
        """Checks user's answer choice with correct answer"""
        if user_choice.lower() == correct_answer.lower():
            self.score += 1  # adds a score of one to total score if answer choice is correct
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    # TODO: checking if we're the end of quiz
    def final_score_report(self):
        print("You have completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")