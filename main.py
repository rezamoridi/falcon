from fastapi import FastAPI
from modoles import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {
        'message': 'Hello World',
    }

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {
        'todos': todos,
        }
# Get single todos

# Create a todo
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {
        'message': 'Todo Has Been Added',
        }
# Update a todo
