from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Inbox
from accounts.models import Engineer
from django.views.generic.list import ListView


class CreateMessage(CreateView):
    model = Inbox
    template_name = "../templates/message.html"
    fields = "__all__"

    def get_success_url(self):
        pass

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=False)
            form.instance.engineer = self.request.user
            form.save()
            return redirect("inbox", pk=self.request.user.id)
        return super(CreateMessage, self).form_valid(form)


class AllMessages(ListView):
    model = Inbox
    context_object_name = "mails"
    template_name = "../templates/message.html"
