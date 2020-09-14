
from django.shortcuts import render

from .models import Area, Level
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'dws/index.html'
    context_object_name = 'areas'
    def get_queryset(self):
        """Return the last five published questions."""
        print('GETTING QUERY SET')
        return Area.objects.all
