from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.title

class Task(models.Model):
    """ Task model """

    author = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    is_finished = models.BooleanField(default=False, blank=True)

    deadline = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    finished = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title


