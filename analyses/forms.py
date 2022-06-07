from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='')


class Answer:

    def __init__(self, answer="default check", links=["default 1", "default 2"], question=""):
        self.answer_text = answer
        self.link_one = links[0]
        self.link_two = links[1]
        self.question = question
