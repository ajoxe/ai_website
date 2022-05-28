from django.db import models

class Analysis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    graph = models.FilePathField(path="/graph")
    preview_image = models.FilePathField(path="/img")
