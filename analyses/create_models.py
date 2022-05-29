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
a4 = Analysis(
    name="Calamity by region",
    description="Most Referred Locations Per Calamities",
    graph='graph/disasters_per_location.html',
    preview_image='img/calamity_by_region.png'
)
a4.save()
