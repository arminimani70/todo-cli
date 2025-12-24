# 📝 Python CLI To-Do App

A Python command-line To-Do application with clean architecture and JSON storage.

## Features

- Add new tasks
- Show tasks with status
- Mark tasks as done
- Delete tasks
- Persistent storage using JSON

## Design

This project follows an Object-Oriented Programming (OOP) approach:

- `Task` class represents a single task
- `TaskManager` handles task operations and persistence
- UI logic is separated from business logic

## Project Structure

todo-cli/
├── main.py
├── tasks.json
├── README.md

## How to Run

```bash
python main.py
```
