from django.shortcuts import render
from django.views import View


class PublicationListView(View):
    def get(self, request):
        return render(request, 'publication/list.html')