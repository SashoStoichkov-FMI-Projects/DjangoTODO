from django import forms
from .models import Board, Task, Comment


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["name", "is_team"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "status",
            "importance",
            "person_responsible",
            "due_date",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
