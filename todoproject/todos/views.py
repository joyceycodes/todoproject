from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.

def list_todo_items(request):
    return render(request,'todos/todo_list.html')

def insert_todo_item(request:HttpRequest):
    # django ORM will handle the queries for us    
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list/')