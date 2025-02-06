from django.urls import path
from webapp.views import PublicationListView, PublicationCreateView, LikePublicationView, PublicationDetailView, CommentCreateView


app_name = 'webapp'
urlpatterns = [
    path('', PublicationListView.as_view(), name='publication-list'),
    path('<int:pk>/', PublicationDetailView.as_view(), name='publication-detail'),
    path('create/', PublicationCreateView.as_view(), name='publication-create'),
    path('<int:pk>/like/', LikePublicationView.as_view(), name='like-publication'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment-publication'),
]
