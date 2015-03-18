from django.shortcuts import get_object_or_404, render, render_to_response

from base.models import Project, Task

# Create your views here.
def index(request):
	project_list = Project.objects.order_by('pk')
	#for project in project_list:
	#	project_task = Task.objects.filter(project = project.pk).order_by('-status', 'priority', 'progress')
	context = {'project_list': project_list}
	return render(request, 'index.html', context)

def detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	context = {'task': task}
	return render(request, 'detail.html', context)
