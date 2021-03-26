from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from notes.models import Notes
from notes.serializers import NotesSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def notes_list(request):
    if request.method == 'GET':
        notes = Notes.objects.all()

        name = request.GET.get('name',None)
        if name is not None:
            notes = notes.filter(name__icontains=name)

        notes_serializer = NotesSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False)

    elif request.method == 'POST':
        notes_data = JSONParser().parse(request)
        notes_serializer = NotesSerializer(data = notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse(notes_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(notes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def notes_detail(request, pk):
    try:
        notes = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return JsonResponse({'message':'The note does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        notes_serializer = NotesSerializer(notes)
        return JsonResponse(notes_serializer.data)

    elif request.method == 'PUT':
        notes_data = JSONParser().parse(request)
        notes_serializer = NotesSerializer(notes, data=notes_data)
        if notes_serializer.is_valid():
            notes_serializer.save()
            return JsonResponse(notes_serializer.data)
        return JsonResponse(notes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        notes.delete()
        return JsonResponse({'message':'Notes was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
