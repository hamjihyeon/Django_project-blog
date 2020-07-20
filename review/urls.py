from django.urls import path

from review.views import LikeListView, WhereCreateView, EatCreateView, LikeUpdateView, LikeDeleteView, LikeDetailView, \
    LikeWhereListView, LikeEatListView, LikeWhereStarList4View, LikeWhereStarList5View, LikeWhereStarList3View, \
    LikeWhereStarList2View, LikeWhereStarList1View, LikeWhereStarList0View

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
    path('star5/', LikeWhereStarList5View.as_view(),name='liststar5'),
    path('star4/', LikeWhereStarList4View.as_view(),name='liststar4'),
    path('star3/', LikeWhereStarList3View.as_view(),name='liststar3'),
    path('star2/', LikeWhereStarList2View.as_view(),name='liststar2'),
    path('star1/', LikeWhereStarList1View.as_view(),name='liststar1'),
    path('star0/', LikeWhereStarList0View.as_view(),name='liststar0'),
]
