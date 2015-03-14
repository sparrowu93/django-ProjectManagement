from django.shortcuts import render

from base.models import Project, Task

# Create your views here.
def index(request):
	project_list = Project.objects.order_by('status').order_by('pk')
	context = {'project_list': project_list}
	return render(request, 'index.html', context)