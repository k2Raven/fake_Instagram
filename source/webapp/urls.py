from django.urls import path
from webapp.views import PublicationListView, PublicationCreateView, LikePublicationView


app_name = 'webapp'
urlpatterns = [
    path('', PublicationListView.as_view(), name='publication-list'),
    path('create/', PublicationCreateView.as_view(), name='publication-create'),
    path('<int:pk>/like/', LikePublicationView.as_view(), name='like-publication'),
]
