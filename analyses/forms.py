from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='')


class Answer:

    def __init__(self, answer="", links=["", ""], question=""):
        self.answer_text = answer
        self.link_one = links[0]
        self.link_two = links[1]
        self.question = question
