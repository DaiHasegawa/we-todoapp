from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import datetime

from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise 
from tortoise.contrib.pydantic import pydantic_model_creator
from models import TodoItem

app = FastAPI(title="TODO API", description="TODOリスト管理API", version="1.0.0")

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3001", "http://127.0.0.1:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TortoiseモデルからPydanticモデルを自動生成: include=は必須、exclude=は除外
TodoItem_Pydantic = pydantic_model_creator(TodoItem)
TodoItemCreate_Pydantic = pydantic_model_creator(TodoItem, exclude=("id","completed"))
TodoItemUpdate_Pydantic = pydantic_model_creator(TodoItem, exclude=("id",))

@app.get( "/" ) 
def read_root (): 
    return { "message" : "TODO APIへようこそ！" } 

@app.get( "/todos" , response_model= List [TodoItem_Pydantic] ) 
async def get_all_todo(): 
    todos = await TodoItem.all()
    return todos

@app.get( "/todos/{todo_id}" , response_model=TodoItem_Pydantic ) 
async def get_todo ( todo_id: int):
    todo = await TodoItem.get(id=todo_id) 
    if todo: 
        return todo 
    raise HTTPException(status_code= 404 , detail= "TODOが見つからない" )


@app.post("/todos", response_model=TodoItem_Pydantic)
async def create_todo(req: TodoItemCreate_Pydantic):
    new_todo = await TodoItem.create(title=req.title, description=req.description)
    
    return new_todo

@app.delete( "/todos/{todo_id}") 
async def delete_todo ( todo_id: int): 
    todo = await TodoItem.get(id=todo_id)
    if todo:
        await todo.delete()
        return {"message": f"TODOを削除しました"}
    raise HTTPException(status_code= 404 , detail= "TODOが見つからない" )


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, req: TodoItemUpdate_Pydantic):
    for i, todo in enumerate(todos): 
        if todo.id == todo_id: 
            todo.title = req.title if req.title is not None else todo.title 
            todo.description = req.description if req.description is not None else todo.description
            todo.completed = req.completed if req.completed is not None else todo.completed
            return todo
    raise HTTPException(status_code= 404 , detail= "TODOが見つからない" )


register_tortoise( 
    app, 
    db_url="sqlite://db.sqlite3", 
    modules={"models": ["models"]}, 
    generate_schemas=True, 
    add_exception_handlers=True,
    )