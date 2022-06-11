from django.shortcuts import render
from rest_framework.response import Response

from .serializers import NoteSerializer
from rest_framework.decorators import api_view
from .models import Note


# Create your views here.
@api_view(["GET", "POST"])
def notes(request):
    if request.method == "GET":
        return Response(NoteSerializer(Note.objects.all(), many=True).data)

    if request.method == "POST":
        serializer = NoteSerializer(date=request.data, many=False)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def change_complete_state_note(request, pk):
    note = Note.objects.get(id=pk)
    note.change_completed_state()

    if request.method == "GET":
        return Response(NoteSerializer(note, many=False).data)

    if request.method == "PUT":
        return Response(status=200)

    if request.method == "DELETE":
        note.delete()
        return Response(status=200)
