from django.urls import path
from cars.ad.views import ShowAdsView, AdEditView, AdDetailsView, AdDeleteView, \
    CreateDeleteBookmarkView, ListBookmarksView, remove_bookmark, AdCreateView
from .signals import *

urlpatterns = [
    path('ads/', ShowAdsView.as_view(), name='show ads'),
    path('create/', AdCreateView.as_view(), name='create ad'),
    path('edit/<int:pk>/', AdEditView.as_view(), name='edit ad'),
    path('details/<int:pk>/', AdDetailsView.as_view(), name='details ad'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='delete ad'),
    path('bookmark/', CreateDeleteBookmarkView.as_view(), name='bookmark ad'),
    path('bookmarks/', ListBookmarksView.as_view(), name='list bookmarks'),
    path('bookmarks/remove/<int:pk>/', remove_bookmark, name='remove bookmark')
]
