from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import Engineer, Message
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, UpdateView, CreateView
from .forms import EngineerCreationForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EngineerForm
from django.http import HttpResponse
from django.core.serializers import serialize


def django_models_json(request, pk):
    qs = Engineer.objects.get(id=pk)
    # qs = Engineer.objects.first()
    data = serialize("json", [qs], fields=("username", "email", "tech_stack"))
    return HttpResponse(data, content_type="application/json")


class LoginUser(LoginView):
    model = Engineer
    redirect_authenticated_user = True
    template_name = "../templates/login.html"

    def get_success_url(self):
        return reverse("profile", args=[self.request.user.id])


class UserSignUp(FormView):
    form_class = EngineerCreationForm
    template_name = "../templates/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect("login")
        return super(UserSignUp, self).form_valid(form)

    """
    to redirect authenticated users
    """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("all_projects")
        return super(UserSignUp, self).get(request)


# ....................... Engineer Profile .....................
class EngineerProfile(DetailView):
    model = Engineer
    template_name = "../templates/profile.html"


class EngineerProject(DetailView):
    """
    All Engineer's project set to public
    """

    model = Engineer
    template_name = "../templates/projects.html"

    def get_context_data(self, **kwargs):
        context = super(EngineerProject, self).get_context_data()
        pk = self.kwargs.get("pk")
        context["engineer"] = Engineer.objects.get(id=pk)
        context["public_projects"] = context["engineer"].project_set.filter(
            make_public=True
        )
        return context


class PrivateProjects(DetailView):
    """
    All Engineer's project set to private
    """

    model = Engineer
    template_name = "../templates/private.html"

    def get_context_data(self, **kwargs):
        context = super(PrivateProjects, self).get_context_data()
        pk = self.kwargs.get("pk")
        context["engineer"] = Engineer.objects.get(id=pk)
        context["private_projects"] = context["engineer"].project_set.filter(
            make_public=False
        )
        return context


class EngineerSettings(LoginRequiredMixin, UpdateView):
    model = Engineer
    template_name = "../templates/settings.html"
    form_class = EngineerForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect("profile", pk=self.request.user.id)
        return super(EngineerSettings, self).form_valid(form)
# only engineers should be able to update their profile


class CreateMessage(CreateView):
    model = Message
    template_name = '../templates/create-message.html'
