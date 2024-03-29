from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    #site_1/lotto/templates/lotto/default.html
    return render(request, 'lotto/default.html', {'lottos':lottos})#{}는 재활용위함
    #-> site_1\lotto\templates\lotto\default.html

def hello(request):
    return HttpResponse("<h1 style = 'color:red; ' >Hello, world! </h1>")
# request.method == 'GET'
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
