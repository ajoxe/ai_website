from django.shortcuts import render
from analyses.models import Analysis
from django.contrib.staticfiles import finders
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import QuestionForm
from .forms import Answer
from django import forms
from .query import search


# Returns short form card view for analysis. Used in carousel and all analyses page.
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


# Returns long form full detail page for analysis.
def analysis_detail(request, pk):
    analyses = Analysis.objects.all()
    analysis = Analysis.objects.get(pk=pk)
    file_handle = finders.find(analysis.graph)
    with open(file_handle, 'r') as f:
        contents = f.read()
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


# Returns a list of all analysis graphs as analysis_index card views
def analysis_all(request):
    analyses = Analysis.objects.all()
    context = {
        'analyses': analyses
    }
    return render(request, 'analysis_all.html', context)


# Used for ask_ai page, returns an answer to a query as well as the initial empty state for the page.
# NB: Embedded apps will not work in Safari. Please use Chrome instead.
def get_answer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        answer_form = Answer()
        if form.is_valid():
            question = form.cleaned_data.get("question")
            answers = search(question)
            answer_form = Answer(answers, question)
        # We'll clear the form after processing and return the query results
        return render(request, 'ask_ai.html', {'form': QuestionForm(), 'answer': answer_form})
    else:
        # For the initial page request, we set the form and answer to an empty state.
        form = QuestionForm()
        answer = Answer()

    return render(request, 'ask_ai.html', {'form': form, 'answer': answer})


# Returns embedded active learner labeling app.
# NB: Embedded apps will not work in Safari
def get_active_learner(request):
    return render(request, 'active_learner_labeling_app.html')
