from django.shortcuts import render, redirect
from tasks.forms import BoardForm, TaskForm, CommentForm
from tasks.models import Board, Task, Comment


def list_boards(request):
    boards = Board.objects.all()
    return render(request, "tasks/list_boards.html", {"boards": boards})


def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/boards")
    else:
        form = BoardForm()
    return render(request, "tasks/create_board.html", {"form": form})


def export_board(request, pk):
    board = Board.objects.get(pk=pk)
    tasks = Task.objects.filter(board=board)
    comments = Comment.objects.filter(task__in=tasks)
    data = {
        "board": {
            "name": board.name,
        },
        "tasks": [
            {
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "comments": [
                    {
                        "text": comment.text,
                    }
                    for comment in comments
                    if comment.task == task
                ],
            }
            for task in tasks
        ],
    }
    return render(request, "tasks/export_board.html", {"data": data})


def import_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            return redirect(f"/tasks/boards/{board.pk}/tasks")
    else:
        form = BoardForm()
    return render(request, "tasks/import_board.html", {"form": form})


def update_board(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect("/tasks/boards")
    else:
        form = BoardForm(instance=board)
    return render(request, "tasks/update_board.html", {"form": form, "board": board})


def delete_board(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect("/tasks/boards")


def list_tasks(request, pk):
    board = Board.objects.get(pk=pk)
    tasks = Task.objects.filter(board=board)
    return render(request, "tasks/list_tasks.html", {"tasks": tasks, "board": board})


def create_task(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.board = board
            task.save()
            return redirect(f"/tasks/boards/{board.pk}/tasks")
    else:
        form = TaskForm()
    return render(request, "tasks/create_task.html", {"form": form, "board": board})


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    comments = Comment.objects.filter(task=task)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect(f"/tasks/{task.pk}")
    else:
        form = CommentForm()
    return render(
        request,
        "tasks/task_detail.html",
        {"task": task, "form": form, "comments": comments},
    )


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"/tasks/{task.pk}")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/update_task.html", {"form": form, "task": task})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect(f"/tasks/boards/{task.board.pk}/tasks")


def list_comments(request, pk):
    task = Task.objects.get(pk=pk)
    comments = Comment.objects.filter(task=task)
    return render(
        request, "tasks/list_comments.html", {"comments": comments, "task": task}
    )


def add_comment(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect(f"/tasks/{task.pk}")
    else:
        form = CommentForm()
    return render(request, "tasks/add_comment.html", {"form": form, "task": task})


def delete_comment(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect(f"/tasks/{pk}")
