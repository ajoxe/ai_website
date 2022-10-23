#!/bin/bash
from analyses.models import Analysis


# Adds analyses for website. This list will be iterated in order and will appear in the analysis carousel at the bottom
# of the site as well as the All Analyses page in navigation
#
# Updating existing graph:
# If you would like to update an existing graph, you can simply swap out the existing file for the updated one, ensuring
# it has the exact same file name. You can determine what the file name is from the list below, set to the field `graph`
# you will not need to worry about updating the db for this kind of task since you are only swapping out the data, not
# the pointer.
#
# Adding a new graph:
# If you would like to add a new graph, that has not previously existed, you can simply add it to the bottom. You can
# copy/paste the overall model template. You will need to add your graph html file to `analyses/static/graph'. You will
# also need to screenshot your graph as a preview image and add the png screenshot file to 'analyses/static/img'.
# Please provide a name and description for your graph so the UI can continue to look decent.
# After adding your files, emphasis on after, you will need to run the django migration script
# and only add that single graph. You can do this easily using the add_new_analysis() function in
# `python manage.py shell` interactive console. Looks like this:
# >>> from analyses.models import Analysis
# >>> import analyses.create_models as create
# >>> create.add_new_analyses(...)
# >>> exit()
# At this point you should add your new graph to the running list of graphs, so that it does not get missed when the db
# gets updated.
#
# Inserting or reordering graphs:
# If you want to change the order of the graphs or insert a graph, you will need to flush the db (delete everything)
# and run add_analyses() all over again, ensuring the new graph is in that function. Yes, this is not ideal but for now
# our numbers are low enough that this should not be an issue. I'll make it nice when we get famous.
#
# If you're at all uncertain, please contact AJ Oxendine
def add_all_analyses():
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
        name="Explore Papers on Natural Disasters",
        description="Demo based on 8000 papers realated to natural disasters plotted into 2 dimensions",
        graph='graph/explore_papers.html',
        preview_image='img/explore_papers.png'
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
        name="Top Researchers per Calamity",
        description="Top Researchers per Calamity per author",
        graph='graph/top_researchers_per_calamity.html',
        preview_image='img/top_researchers_per_calamity.png'
    )
    a7.save()

    a8 = Analysis(
        name="K-Means Clustering of Natural Disaster papers",
        description="Papers of the same color represent a cluster of similar theme. Papers appearing closer together are closer in content.",
        graph='graph/research_paper_clusters.html',
        preview_image='img/research_paper_clustering.png'
    )
    a8.save()


NEXT_ANALYSIS = 9


def add_new_analysis(name, description, graph, preview_image):
    new_analysis = Analysis(
        name=name or "",
        description=description or "",
        graph=graph or "",
        preview_image=preview_image or ""
    )
    new_analysis.save()



