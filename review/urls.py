from django.urls import path

from review.views import LikeListView, WhereCreateView, EatCreateView, LikeUpdateView, LikeDeleteView, LikeDetailView, \
    LikeWhereListView, LikeEatListView

app_name = 'review'

urlpatterns = [
    path('', LikeListView.as_view(),name='list'),
    path('add_where/', WhereCreateView.as_view(),name='add_where'),
    path('add_eat/', EatCreateView.as_view(),name='add_eat'),
    path('detail/<int:pk>', LikeDetailView.as_view(),name='detail'),
    path('update/<int:pk>/', LikeUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', LikeDeleteView.as_view(),name='delete'),
    path('where/', LikeWhereListView.as_view(),name='listwhere'),
    path('eat/', LikeEatListView.as_view(),name='listeat'),
]
