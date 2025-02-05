from django.urls import path
from webapp.views import PublicationListView


app_name = 'webapp'
urlpatterns = [
    path('', PublicationListView.as_view(), name='publication-list'),
]
