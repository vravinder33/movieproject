from django.shortcuts import render
from testApp.forms import MovieForm
from testApp.models import Movie

# Create your views here.
def indexView(request):
    return render(request,'testapp/home.html')

def addMovieView(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return indexView(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def listView(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/movielist.html',{'movielist':movie_list})
