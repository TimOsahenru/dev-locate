from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Inbox
from accounts.models import Engineer
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateMessage(LoginRequiredMixin, CreateView):
    model = Inbox
    template_name = "../templates/create-message.html"
    fields = ["body"]

    # def get_context_data(self, **kwargs):
    #     context = super(CreateMessage, self).get_context_data()
    #     pk = self.kwargs.get('pk')
    #     context['engineer'] = Engineer.objects.get(id=pk)
    #     context['mails'] = Inbox.objects.filter(sender=self.request.user)
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(CreateMessage, self).get_context_data()
    #     pk = self.kwargs.get("pk")
    #     context["engineer"] = Engineer.objects.get(id=pk)
    #     context["mails"] = context["mail"].receiver_set.all()
    #     # context["mails"] = context["mail"].engineer.mail_sender.all()
    #     # context["mails"] = context["engineer"].inbox_set.all()
    #     return context

    def get_success_url(self):
        pass

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=False)
            form.instance.sender = self.request.user
            form.save()
            return redirect("create-message", pk=self.request.user.id)
        return super(CreateMessage, self).form_valid(form)


# class AllMessages(ListView):
#     model = Inbox
#     context_object_name = "mails"
#     template_name = "../templates/message.html"
