from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html')


def ps3_collection(request):
    return render(request, 'ps3_collection.html')


def standard_games(request):
    return render(request, 'standard_games.html')
