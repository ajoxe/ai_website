from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='')


class Answer:

    def __init__(self, answers=["", ""], links=["", ""], question=""):
        self.answer_one = answers[0]
        self.answer_two = answers[1]
        self.link_one = links[0]
        self.link_two = links[1]
        self.question = question
