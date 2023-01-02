from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("boards", views.list_boards, name="list_boards"),
    path("boards/create", views.create_board, name="create_board"),
    path("boards/<int:pk>/update", views.update_board, name="update_board"),
    path("boards/<int:pk>/delete", views.delete_board, name="delete_board"),
    path("boards/<int:pk>/tasks", views.list_tasks, name="list_tasks"),
    path("boards/<int:pk>/tasks/create", views.create_task, name="create_task"),

    path("<int:pk>", views.task_detail, name="task_detail"),
    path("<int:pk>/update", views.update_task, name="update_task"),
    path("<int:pk>/delete", views.delete_task, name="delete_task"),
    path("<int:pk>/comments", views.list_comments, name="list_comments"),
    path("<int:pk>/comments/create", views.add_comment, name="add_comment"),
    path(
        "<int:pk>/comments/<int:comment_pk>/delete",
        views.delete_comment,
        name="delete_comment",
    ),
]
