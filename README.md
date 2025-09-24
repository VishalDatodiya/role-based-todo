# 📝 Role-Based ToDo App (Django Rest Framework)

A modern **Task Management API** built with **Django Rest Framework (DRF)**.  
Implements **Role-Based Access Control (RBAC)**, task assignments, comments, and email notifications with **Celery + Redis**.  

---

## 🚀 Features

### 👤 Authentication & User Roles
- JWT-based authentication (login, register, logout)  
- Roles: **Admin**, **Manager**, **Employee**  
- Role-based access control (RBAC) with custom permissions  

### ✅ Task Management
- Create, update, delete, list tasks  
- Assign tasks to multiple users (via `UserTask` mapping)  
- Task filtering, search, ordering, pagination  
- Due date support  

### 💬 Comments
- Employees can comment on their assigned tasks  
- RBAC: only owners can update/delete their comments  

### 🔔 Notifications
- Email notification when a task is assigned  
- Reminder email **1 day before due date** (Celery beat scheduler)  

### ⚙️ Extra Features
- API response time tracking  
- Secure environment variables (`.env`)  
- Unit testing (API + permissions)  

---

## 🛠 Tech Stack
- **Backend**: Django, Django Rest Framework  
- **Database**: PostgreSQL / MySQL (configurable)  
- **Auth**: JWT (SimpleJWT)  
- **Background Jobs**: Celery + Redis  
- **Scheduler**: Celery Beat  
- **Environment Management**: python-decouple  
- **Testing**: Django TestCase / DRF APITestCase  

---

## ⚡ Setup & Installation

1. **Clone repo**
```bash
git clone https://github.com/yourusername/role-based-todo.git
cd role-based-todo

