# 📝 Minimal TODO List
### Django • Class-Based Views • Server-Rendered • Dockerized

A **minimal, clean, and well-architected TODO List** built with  
**Django Class-Based Views (CBV)** and **Django Templates**.

This repository is intentionally designed as a **reference-ready mini project**
to practice correct Django architecture — not just to “make it work”.

---

## 🧭 Project Overview
User

└── Authentication (Login / Logout)

└── Task List (Single Page)

├── View tasks

├── Create task

├── Toggle done / undone

├── Edit task

└── Delete task

text

- Fully server-rendered
- No JavaScript
- One main page for the core workflow
- Clean separation of concerns using CBVs

---

## 🎯 Project Philosophy

> **Minimal Code — Correct Architecture**

The focus of this project is:
- clarity over cleverness
- Django best practices
- maintainability over feature count

No over-engineering.  
No unnecessary abstractions.  
Just clean, readable Django.

---

## 🚀 Goals

- Refresh Django fundamentals
- Practice Class-Based Views (CBV)
- Understand CBV composition & MRO
- Implement object-level access control
- Use Docker for consistent development
- Prepare the codebase for Django REST Framework (DRF)

---

## ✅ Features

- User authentication (Login / Logout)
- User-scoped task list
- Create tasks from the main page
- Edit existing tasks
- Delete tasks with confirmation
- Mark tasks as done / undone
- Clean UI using Django Templates
- Fully server-rendered (no JS)
- Dockerized setup

---

## 🧠 Architecture

### Core Views

| View | Responsibility |
|------|----------------|
| `TaskListView` | List + create tasks |
| `TaskToggleDoneView` | Toggle task completion |
| `TaskUpdateView` | Update task |
| `TaskDeleteView` | Delete task |

### Key Concepts

- `LoginRequiredMixin` for access control
- `FormMixin` for handling forms inside list views
- `ListView` for querying and rendering
- Object-level filtering using `request.user`

---

## 🔐 Security

- Authentication required for all task views
- Tasks are strictly scoped to the logged-in user
- Direct object access is prevented

---

## 🧱 Tech Stack

- Python
- Django
- Django Class-Based Views (CBV)
- Django Templates
- SQLite (default)
- Docker & Docker Compose

---

## 🐳 Docker

This project uses Docker for a consistent development environment.

### Services

- Django web application

### Benefits

- No local environment conflicts
- One-command startup
- Reproducible setup
- Production-friendly workflow

---

## ▶️ Run with Docker
```bash
docker compose up --build
```
Then open:

```text
http://localhost:8000
```

---

## ▶️ Run Locally (Without Docker)
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
python base/manage.py migrate
python base/manage.py runserver
```
---

## 🧪 Manual Test Checklist
[ ] Register a user
[ ] Login
[ ] Create a task
[ ] Edit a task
[ ] Toggle task done/undone
[ ] Delete a task
[ ] Verify tasks are user-specific
📦 Future Improvements
Add automated tests
Introduce Django REST Framework (DRF)
API authentication
PostgreSQL support
Redis / caching
Production Docker setup

--- 

## 🏁 Final Notes
This is not a tutorial

and not a production application.

It is a clean Django reference project intended to:

reinforce core Django concepts
demonstrate correct CBV usage
serve as a reusable project template

Built with ❤️ and Django






