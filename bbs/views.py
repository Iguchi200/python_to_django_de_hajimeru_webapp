from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bbs.models import Article

class IndexView(ListView):
  model = Article
  template_name = "bbs/index.html"

class DetailView(DetailView):
  model = Article
  template_name = "bbs/detail.html"

class CreateView(CreateView):
  model = Article
  template_name = "bbs/create.html"
  fields = "__all__"

class UpdateView(UpdateView):
  model = Article
  template_name = "bbs/create.html"
  fields = "__all__"

class DeleteView(DeleteView):
  model = Article
  template_name = "bbs/delete.html"
  success_url = reverse_lazy("bbs:index")
