from django.shortcuts import render
from .models import Streams, Channel, BotAccounts, Binds
from .forms import ChannelForm, StreamForm, BotForm, BindForm
from .link_handler import transformate, stream_validator


def index(request):
    last_stream = str(Streams.objects.last())
    last_stream = transformate(last_stream)
    channels = Channel.objects.all()
    if request.method == "POST":
        chanel_form = ChannelForm(request.POST)
        stream_form = StreamForm(request.POST)
        if chanel_form.is_valid():
            chanel_form.save()
        if stream_form.is_valid() and stream_validator(stream_form.cleaned_data['stream_url']):
            Streams.objects.all().delete()
            stream_form.save()
    else:
        chanel_form = ChannelForm()
        stream_form = StreamForm()
    context = {
        'chanel_form': chanel_form,
        'stream_form': stream_form,
        'last_stream_url': last_stream,
        'chanels': channels,
    }
    return render(request, 'index.html', context=context)


def bots(request):
    bots = BotAccounts.objects.all()
    if request.method == "POST":
        bot_form = BotForm(request.POST)
        if bot_form.is_valid():
            bot_form.save()
    else:
        bot_form = BotForm()
    context = {
        'bot_form': bot_form,
        'Bots': bots
    }
    return render(request, 'bots.html', context=context)


def binds(request):
    bind = Binds.objects.all()
    if request.method == "POST":
        bind_form = BindForm(request.POST)
        if bind_form.is_valid():
            bind_form.save()
    else:
        bind_form = BindForm()
    context = {
        'bind_form': bind_form,
        'bind': bind
    }
    return render(request, 'binds.html', context=context)
