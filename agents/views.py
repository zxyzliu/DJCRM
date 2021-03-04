from django.shortcuts import render
from django.views import generic
from django.shortcuts import reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import AdminLoginRequiredMixin


# Create your views here.

class AgentListView(AdminLoginRequiredMixin, generic.ListView):
    template_name = "agent_list.html"
    context_object_name = 'agents'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(AdminLoginRequiredMixin, generic.CreateView):
    template_name = "agent_create.html"

    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:allList")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(AdminLoginRequiredMixin, generic.DetailView):
    template_name = "agent_detail.html"
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentUpdateView(AdminLoginRequiredMixin, generic.UpdateView):
    template_name = "agent_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse("agents:allList")


class AgentDeleteView(AdminLoginRequiredMixin, generic.DeleteView):
    template_name = "agent_delete.html"
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse("agents:allList")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
