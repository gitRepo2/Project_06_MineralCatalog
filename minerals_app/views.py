from django.shortcuts import get_object_or_404, render
from django.db.models import Count, Q
from django.contrib.auth.models import User
import random
from .models import Minerals


def mineral_list(request):
    """list view, all of the minerals_app"""
    minerals = Minerals.objects.all()
    random_key = random.randint(1, len(minerals))
    return render(request, 'minerals_app/mineral_list.html',
                  {'minerals': minerals,
                   'randomKey': random_key})


def mineral_detail(request, pk):
    """detail view of a mineral"""
    mineral = get_object_or_404(Minerals, pk=pk)
    return render(request, 'minerals_app/mineral_detail.html',
                  {'mineral': mineral})

