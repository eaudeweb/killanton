from django.contrib import admin

from models import Task, Project

class ProjectAdmin(admin.ModelAdmin):
    """ """

class TaskAdmin(admin.ModelAdmin):
    """ """
    list_display = ('id', 'title', 'author', 'project', 'created', 'deadline',
            'finished', 'is_finished', )
    list_filter = ('project', 'author', 'is_finished')
    ordering = ('-created', )
    date_hierarchy = 'created'
    search_fields = ('title', 'description', )

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
