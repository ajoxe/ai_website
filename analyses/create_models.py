from analyses.models import Analysis

a1 = Analysis(
    name="Machine Learning Papers Per year",
    description="Graph of papers on machine learning",
    graph='graph/machine_learning_papers.html',
    secondary_graph='graph/machine_learning_papers_high_level.html',
    preview_image='img/machine_learning_papers.png'
)
a1.save()

a2 = Analysis(
    name="Choropleth Calamity By Region",
    description="Most Referred Locations Per Calamities",
    graph='graph/choropleth_calamity_by_region.html',
    preview_image='img/choropleth_calamity_by_region.png'
)
a2.save()

a3 = Analysis(
    name="Inter-topic Distance Map",
    description="Inter-topic distance map via multidimensional scaling",
    graph='graph/topic_model.html',
    preview_image='img/inter_topic_distance_map.png'
)
a3.save()

a4 = Analysis(
    name="Natural Disaster Papers per year",
    description="Research Papers Per Year On Natural Disasters",
    graph='graph/natural_disaster_papers.html',
    secondary_graph='graph/natural_disaster_papers_stacked.html',
    preview_image='img/natural_disaster_papers.png'
)
a4.save()

a5 = Analysis(
    name="Top Researchers per Calamity",
    description="Top Researchers per Calamity per author",
    graph='graph/top_researchers_per_calamity.html',
    preview_image='img/top_researchers_per_calamity.png'
)
a5.save()

a6 = Analysis(
    name="Tools per Calamity",
    description="Tools per Calamity",
    graph='graph/tools_per_calamity.html',
    preview_image='img/tools_per_calamity.png'
)
a6.save()

a7 = Analysis(
    name="K-Means Clustering of Natural Disaster papers",
    description="Papers of the same color represent a cluster of similar theme. Papers appearing closer together are closer in content.",
    graph='graph/research_paper_clusters.html',
    preview_image='img/research_paper_clustering.png'
)
a7.save()
