from django.shortcuts import render
from analyses.models import Analysis


def analysis_index(request):
    analyses = Analysis.objects.all()
    context = {
        'analyses': analyses
    }
    return render(request, 'analysis_index.html', context)


def analysis_detail(request, pk):
    analysis = Analysis.objects.get(pk=pk)
    context = {
        'analysis': analysis
    }
    return render(request, 'analysis_detail.html', context)
