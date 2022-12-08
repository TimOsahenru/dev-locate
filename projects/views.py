from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Project
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Engineer
from django.db.models import Q
from django.http import HttpResponse
from django.core.serializers import serialize


def django_models_json(request):
    qs = Engineer.objects.first()
    data = serialize("json", [qs], fields=("username", "email", "tech_stack"))
    return HttpResponse(data, content_type="application/json")


class AllProjects(ListView):
    """
    All projects listed on a single page
    """

    model = Project
    context_object_name = "projects"
    template_name = "../templates/index.html"

    def get_context_data(self, **kwargs):
        context = super(AllProjects, self).get_context_data()
        context["projects"] = Project.objects.filter(make_public=True)
        context["engineer_count"] = Engineer.objects.all().count()

        q = self.request.GET.get("q") or ""
        if q:
            context["projects"] = context["projects"].filter(
                Q(engineer__country__icontains=q)
                | Q(engineer__username__icontains=q)
                | Q(engineer__tech_stack__icontains=q)
            )
        return context

    def get_queryset(self):
        return Project.objects.filter(make_public=True)


class ProjectDetail(DetailView):
    model = Project
    template_name = "../templates/detail.html"


class ProjectEdit(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "../templates/edit.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("profile", args=[self.request.user.id])


# to ensure only creators can edit their projects


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "../templates/create.html"
    form_class = ProjectForm
    success_url = reverse_lazy("all_projects")

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=False)
            form.instance.engineer = self.request.user
            form.save()
            return redirect("profile", pk=self.request.user.id)
        return super(ProjectCreate, self).form_valid(form)


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "../templates/delete.html"

    def get_success_url(self):
        return reverse("profile", args=[self.request.user.id])

    # to ensure only creators can delete their projects
