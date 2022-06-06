from django.db import models


class Analysis(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    graph = models.FilePathField(path="/graph", default='plotly.html')
    secondary_graph = models.FilePathField(path="/graph", default='plotly.html')
    preview_image = models.FilePathField(path="/img", default='logo.png')
