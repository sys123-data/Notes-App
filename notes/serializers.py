from rest_framework import serializers
from notes.models import Notes

class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ('id','name','item01','item02','item03','item04','item05','item06','item07','item08','item09','item10')
