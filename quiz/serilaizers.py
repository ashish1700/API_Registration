from rest_framework import serializers
from quiz.models import Questions, Videoo, Testing_image, VideoFestival

class Videooserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Videoo
        fields = ['id','name','video','thumbnail']


class Questionserializer(serializers.ModelSerializer):
    # video_name = serializers.SerializerMethodField(read_only=True)
    # video = Videooserializer(read_only=True)
    # video = serializers.PrimaryKeyRelatedField(queryset=Videoo.objects.all())
    # video_name = serializers.SerializerMethodField(read_only=True)
    video = serializers.PrimaryKeyRelatedField(queryset=Videoo.objects.all())
    video_details = serializers.SerializerMethodField(read_only=True)
    
    # def get_video_name(self, obj):
    #     return obj.video.name
    def get_video_details(self, obj): 
        video = Videoo.objects.get(id=obj.video.id)
        serializer = Videooserializer(video)
        return serializer.data
    
    class Meta:
        model = Questions
        fields = ['video', 'id', 'question', 'option1', 'option2', 'answer', 'video_details']
        # fields = ['id', 'question', 'option1','option2','answer','video','video_name']
        # fields = ['id', 'question', 'option1', 'option2', 'answer', 'video']



class TestingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing_image
        fields = '__all__'


class VideoFestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFestival
        fields = '__all__'