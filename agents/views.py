from django.shortcuts import render
from django.views import generic
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm


# Create your views here.

class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agent_list.html"
    context_object_name = 'agents'

    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agent_create.html"

    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:allList")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agent_detail.html"
    context_object_name = 'agent'

    def get_queryset(self):
        return Agent.objects.all()


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self):
        return reverse("agents:allList")


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agent_delete.html"
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse("agents:allList")

    def get_queryset(self):
        return Agent.objects.all()
