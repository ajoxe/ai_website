from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    description = models.TextField()
    graph = models.FilePathField(path="/graph")
    preview_image = models.FilePathField(path="/img")
