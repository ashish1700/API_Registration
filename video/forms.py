from django import forms  
from video.models import Video
class VideoForm(forms.ModelForm):  
    class Meta:  
        model = Video  
        fields = "__all__" 
        
        # widgets = {'agegroup': forms.TextInput(attrs={'class':'form-control'}),
        #            'subject': forms.TextInput(attrs={'class':'form-control'}),
        #            'topic': forms.TextInput(attrs={'class':'form-control'}),
        #            'video': forms.TextInput(attrs={'class':'form-control'}),
        # }
        
class AddForm(forms.ModelForm):
    
    class Meta:
        model = Video
        fields = ('agegroup','subject','topic','video')