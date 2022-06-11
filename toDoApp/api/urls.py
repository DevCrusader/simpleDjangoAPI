from django.urls import path
from .views import notes, change_complete_state_note

urlpatterns = [
    path("notes/", notes),
    path("notes/<int:pk>/", change_complete_state_note)
]
