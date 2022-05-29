from analyses.models import Analysis

a1 = Analysis(
    name="K-Means Clustering of Natural Disaster papers",
    description="Papers of the same color represent a cluster of similar theme. Papers appearing closer together are closer in content.",
    graph='graph/research_paper_clusters.html',
    preview_image='img/research_paper_clustering.png'
)
a1.save()
a2 = Analysis(
    name="Topic Model of papers",
    description="Topic Model of papers",
    graph='graph/topic_model.html',
    preview_image='img/topic_model.png'
)
a2.save()
a3 = Analysis(
    name="Research Papers Per Year On Natural Disasters",
    description="Research Papers Per Year On Natural Disasters",
    graph='graph/papers_per_year.html',
    preview_image='img/papers_per_year.png'
)
a3.save()
