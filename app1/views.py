from django.shortcuts import render
from .models import *


def player(request):

    data = {
        'players':Player.objects.all().order_by('-t_money')
    }
    return render(request,'players.html',data)
def latest(request):
    data = {
        'trans':Transfer.objects.filter(season='22/23')
    }
    return render(request,'latest-transfers.html',data)


def tryouts(request):
    return render(request,'tryouts.html')

def about(request):
    return render(request,'about.html')
def header(request):
    return render(request,'header.html')

def t_archive(request):
    seasons = []
    for i in Transfer.objects.all().values('season').distinct():
        seasons.append(i['season'])
    print(seasons)
    data = {
        'mavsumlar':sorted(seasons)
    }
    return render(request, 'transfer-archive.html', data)

def season_t(sorov,num):
    data = {
        'seasons':Transfer.objects.filter(season__startswith=num).order_by("-money")
    }
    return render(sorov,'2017-18season.html',data)

def country_c(request,name):
    data = {
        'clubs':Club.objects.filter(country=name.capitalize())
    }
    return render(request,'england.html',data)
def clubs(request):
    data = {
        'clubs':Club.objects.all()
    }
    return render(request,'clubs.html',data)
def country_club(request,name):
    data = {
        'c_player':Player.objects.filter(p_name=name)
    }
    return render(request,'country-clubs.html',data)
def u_20(request):
    data = {
        'yoshlar':Player.objects.filter(p_age__lt = 20).order_by('-t_money')
    }
    return render(request,'U-20 players.html',data)
def transfer_r(request):
    data ={
        't_records':Transfer.objects.filter(money__gt = 50).order_by('money')
    }
    return render(request,'transfer-records.html',data)

