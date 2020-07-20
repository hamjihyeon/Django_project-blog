from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, ListView, DetailView

from review.models import Like, Eat, Where


class LikeListView(ListView):
    model = Like


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

class LikeDetailView(DetailView):
    model = Like
    success_url = reverse_lazy('review:list')

class LikeWhereListView(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(category__contains='Where')
        return like_list

class LikeEatListView(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(category__contains='Eat')
        return like_list