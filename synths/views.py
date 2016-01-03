from django.shortcuts import render
from synths.models import Synth
# from IPython import embed

def index(request):
    synths = Synth.objects.all()
    return render(request, 'index.html', {
        'synths': synths,
    })

def detail(request, slug):
    synth = Synth.objects.get(slug=slug)
    return render(request, 'synths/detail.html', {
        'synth': synth,
    })
