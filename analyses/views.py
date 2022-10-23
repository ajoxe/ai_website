from django.shortcuts import render
from analyses.models import Analysis
from django.contrib.staticfiles import finders
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
import json
from urllib.request import build_opener, HTTPCookieProcessor

from .forms import QuestionForm
from .forms import Answer
from django import forms
from .query import search


def analysis_index(request):
    analyses = Analysis.objects.all()
    featured_path = 'graph/plotly.html'
    file_handle = finders.find(featured_path)
    with open(file_handle, 'r') as f:
        contents = f.read()
    context = {
        'analyses': analyses,
        'featured_contents': contents
    }
    return render(request, 'analysis_index.html', context)


def analysis_detail(request, pk):
    analyses = Analysis.objects.all()
    analysis = Analysis.objects.get(pk=pk)
    file_handle = finders.find(analysis.graph)
    # file_handle = finders.find('graph/explore_papers.html')
    with open(file_handle, 'r') as f:
        contents = f.read()
    # url = 'https://octaves0911.streamlitapp.com/octaves0911/streamlit-viz/viz.py'
    # opener = build_opener(HTTPCookieProcessor())
    # response = opener.open(url).read()
    # # print(response)
    # print(response.decode("utf-8"))
    # contents = response.decode("utf-8")
    contents_2 = None
    if analysis.secondary_graph is not None and analysis.secondary_graph != 'plotly.html':
        file_handle = finders.find(analysis.secondary_graph)
        with open(file_handle, 'r') as f:
            contents_2 = f.read()
    graph_contents = [contents]
    if contents_2:
        graph_contents.append(contents_2)
    context = {
        'analysis': analysis,
        'graph_contents': graph_contents,
        'analyses': analyses
    }
    return render(request, 'analysis_detail.html', context)


def analysis_all(request):
    analyses = Analysis.objects.all()
    context = {
        'analyses': analyses
    }
    return render(request, 'analysis_all.html', context)


def get_answer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        answer_form = Answer()
        if form.is_valid():
            question = form.cleaned_data.get("question")
            answer_fields = search(question)
            answer_form = Answer(answer_fields[0], answer_fields[1], question)
        return render(request, 'ask_ai.html', {'form': QuestionForm(), 'answer': answer_form})
    else:
        form = QuestionForm()

    return render(request, 'ask_ai.html', {'form': form, 'answer': Answer()})


def get_active_learner(request):
    return render(request, 'active_learner_labeling_app.html')
