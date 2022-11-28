from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import Engineer
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, UpdateView
from .forms import EngineerCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EngineerForm


# ................ Login User ........................
class LoginUser(LoginView):
    model = Engineer
    redirect_authenticated_user = True
    template_name = '../templates/login.html'

    def get_success_url(self):
        return reverse('profile', args=[self.request.user.id])


# ............................. SignUp User ....................
class UserSignUp(FormView):
    form_class = EngineerCreationForm
    template_name = '../templates/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('login')
        return super(UserSignUp, self).form_valid(form)

# to redirect authenticated users
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('all_projects')
        return super(UserSignUp, self).get(request)


# ....................... Engineer Profile .....................
class EngineerProfile(DetailView):
    model = Engineer
    template_name = '../templates/profile.html'


# ................ Engineer projects .......................
class EngineerProject(DetailView):
    model = Engineer
    template_name = '../templates/projects.html'

    def get_context_data(self, **kwargs):
        context = super(EngineerProject, self).get_context_data()
        pk = self.kwargs.get('pk')
        context['engineer'] = Engineer.objects.get(id=pk)
        context['public_projects'] = context['engineer'].project_set.filter(make_public=True)
        context['private_projects'] = context['engineer'].project_set.filter(make_public=False)
        return context


# ............. Engineer Settings ........................
class EngineerSettings(LoginRequiredMixin, UpdateView):
    model = Engineer
    template_name = '../templates/settings.html'
    form_class = EngineerForm
    
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('profile', pk=self.request.user.id)
        return super(EngineerSettings, self).form_valid(form)

# only engineers should be able to update their profile
