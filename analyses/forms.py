from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='')


class AnswerItem:

    def __init__(self, answer={}):
        self.answer_text = answer.get('answer', "")
        self.answer_link = answer.get('link', "")


class Answer:

    def __init__(self, answers=[], question=""):
        answer_list = []
        for answer in answers:
            answer_list.append(AnswerItem(answer))
        self.question = question
        self.answers = answer_list
