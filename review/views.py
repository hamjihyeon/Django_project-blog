from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView

from review.models import Like, Eat, Where


class LikeListView(ListView):
    model = Like
    paginate_by = 5


class WhereCreateView(CreateView):
    model = Where
    fields = '__all__'
    template_name = 'review/like_create.html'
    success_url = reverse_lazy('review:list')
    initial = {'category': 'Where'}

class EatCreateView(CreateView):
    model = Eat
    fields = '__all__'
    template_name = 'review/like_create.html'
    success_url = reverse_lazy('review:list')
    initial = {'category': 'eat'}

class LikeUpdateView(UpdateView):
    model = Like
    fields = '__all__'
    template_name_suffix = '_update'
    success_url = reverse_lazy('review:list')


class LikeDeleteView(DeleteView):
    model = Like
    success_url = reverse_lazy('review:list')
