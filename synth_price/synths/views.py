from django.shortcuts import render

def index(request):
    # dummy example values
    synth_name = 'SH-101'
    manufacturer = 'Roland'

    return render(request, 'index.html', {
        'synth': synth_name,
        'manufacturer': manufacturer,
        'year': ''
    })
