from django.shortcuts import render
from analyses.models import Analysis

def analysis_index(request):
    analyses = Analysis.objects.all()
    context = {
    'analyses': analyses
    }
    print("*****ANALYSIS")
    print(analyses)
    analysis_1_name = analyses[0].preview_image
    print(analysis_1_name)
    return render(request, 'analysis_index.html', context)

def analysis_detail(request, pk):
    analysis = Analysis.objects.get(pk=pk)
    context = {
    'analysis': analysis
    }
    print("*****ANALYSIS DETAIL")
    return render(request, 'analysis_detail.html', context)
