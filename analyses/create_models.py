from analyses.models import Analysis

a1 = Analysis(
    name="Explorations",
    description="Explore research papers",
    graph='graph/plotly.html',
    preview_image='img/plotly_preview.png'
)
a1.save()
a2 = Analysis(
    name="Topics",
    description="Explore topics",
    graph='graph/topicmodel.html',
    preview_image='img/topic_preview.png'
)
a2.save()
a3 = Analysis(
    name="Knowledge",
    description="test",
    graph='graph/test',
    preview_image='img/test.png'
)
a3.save()
