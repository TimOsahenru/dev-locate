from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Engineer


# ............. All Projects ...............
class AllProjects(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = '../templates/index.html'

    def get_queryset(self):
        public_projects = Project.objects.filter(make_public=True)
        return public_projects


# ............. Detail Project ...............
class ProjectDetail(DetailView):
    model = Project
    template_name = '../templates/detail.html'


# ............. Edit Project ...............
class ProjectEdit(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = '../templates/edit.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('profile', args=[self.request.user.id])

# to ensure only creators can edit their projects


# ............. Create Project ...............
class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = '../templates/create.html'
    form_class = ProjectForm
    success_url = reverse_lazy('all_projects')

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=False)
            form.instance.engineer = self.request.user
            form.save()
            return redirect('profile', pk=self.request.user.id)
        return super(ProjectCreate, self).form_valid(form)


# ............. Delete Project ........................
class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = '../templates/delete.html'

    def get_success_url(self):
        return reverse('profile', args=[self.request.user.id])

    # to ensure only creators can delete their projects
