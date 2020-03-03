from django.urls import path
from wiki.views import PageListView, PageDetailView, PageView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', PageView.as_view(), name='new-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
