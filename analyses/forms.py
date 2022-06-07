from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='Question')


class Answer:

    def __init__(self, answer="default check", links=["default 1", "default 2"]):
        self.answer_text = answer
        self.link_one = links[0]
        self.link_two = links[1]
