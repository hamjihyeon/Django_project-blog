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

class LikeWhereStarList5View(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(star__contains=5)
        return like_list

class LikeWhereStarList4View(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(star__contains=4)
        return like_list

class LikeWhereStarList3View(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(star__contains=3)
        return like_list

class LikeWhereStarList2View(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(star__contains=2)
        return like_list

class LikeWhereStarList1View(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(star__contains=1)
        return like_list

class LikeWhereStarList0View(ListView):
    model = Like
    template_name = 'review/like_list.html'
    def get_queryset(self):
        like_list = self.model.objects.filter(star__contains=0)
        return like_list