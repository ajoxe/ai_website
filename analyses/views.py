from django.shortcuts import render
from analyses.models import Analysis
from django.contrib.staticfiles import finders


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
    analysis = Analysis.objects.get(pk=pk)
    file_handle = finders.find(analysis.graph)
    with open(file_handle, 'r') as f:
        contents = f.read()
    context = {
        'analysis': analysis,
        'graph_contents': contents
    }
    return render(request, 'analysis_detail.html', context)


def analysis_all(request):
    analyses = Analysis.objects.all()
    context = {
        'analyses': analyses
    }
    return render(request, 'analysis_all.html', context)
