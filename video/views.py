from django.shortcuts import render, redirect
from video.models import Video
from video.forms import VideoForm, AddForm
from rest_framework import routers
# from video.serializers import APItestSerializer
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        video = VideoForm(request.POST)
        if video.is_valid():
            ag = video.cleaned_data['agegroup']
            sb = video.cleaned_data['subject']
            to = video.cleaned_data['topic']
            vi = video.cleaned_data['video']
            reg = video(agegroup = ag, subject = sb)
            reg.save()
    else:
        video = VideoForm()
    video=Video.objects.all()
    return render (request, 'index.html', {"video":video})



def addvideoview(request):
    if request.method == 'POST':
        addd = AddForm(request.POST)
        if addd.is_valid():
            addd.save()
            return redirect('/home/')
    else:
        
        
        addd = AddForm()    
    return render(request, 'addvideo.html', {'form':addd})
    
def deleteview(request):
    if request.method == "POST":
        data = request.POST 
        id = data.get('id')
        
        
    



# class APItestViewSet(viewsets.ModelViewSet):
#     serializer_class = APItestSerializer
#     queryset = APItest.objects.all()