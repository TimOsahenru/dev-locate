from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .models import Engineer
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import EngineerCreationForm
from django.views.generic.detail import DetailView


# ................ Login User ........................
class LoginUser(LoginView):
    model = Engineer
    redirect_authenticated_user = True
    template_name = '../templates/login.html'


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

    def get_context_data(self, **kwargs):
        context = super(EngineerProfile, self).get_context_data()
        pk = self.kwargs.get('pk')
        context['engineer'] = Engineer.objects.get(id=pk)
        context['public_projects'] = context['engineer'].project_set.filter(make_public=True)
        context['private_projects'] = context['engineer'].project_set.filter(make_public=False)
        return context


