import random


class Mystery:
    def __init__(self, question, answer, choices):
        self.question = question
        self.answer = answer
        self.choices = choices

    def quiz(self):
        self.choices.append(self.answer)
        random.shuffle(self.choices)
        index = self.choices.index(self.answer)
        print(f"Question:", self.question, end="\n")
        for x, y in enumerate(self.choices):
            print(f"{x}. {y}")
        print(f"Select option:")
        user_answer = int(input())
        if user_answer == index:
            return True
        else:
            return False
