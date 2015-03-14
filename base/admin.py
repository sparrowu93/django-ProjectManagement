# -*- coding: utf-8 -*-

from django.contrib import admin

from base.models import Project, Milestone, Task
# Register your models here.

admin.site.register(Project)
admin.site.register(Milestone)

class TaskAdmin(admin.ModelAdmin):
	list_display = ('category', 'name', 'project', 'priority', 'progress_with_percent_symbol', 'plan_date', 'due_date', 'assign_to', 'status', 'updated_time')



admin.site.register(Task, TaskAdmin)
