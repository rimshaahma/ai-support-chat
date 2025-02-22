
# AI Support Chat - Django Web Application

## 📌 Project Overview
**AI Support Chat** is a Django-based web application designed to facilitate AI-driven chat support. It includes user authentication, real-time messaging, and integration with AI-based assistants.

---

## 🚀 Features
- **User Authentication** (Login, Signup, Logout)
- **AI-Powered Chat Support**
- **Admin Dashboard**
- **Database-Driven Conversations**
- **REST API for Integration**
- **Fully Scalable & Secure**

---

## 📁 Folder Structure
```
ai-support-chat/
│── ai_support/                # Main Django project
│   ├── ai_support/            # Project settings & configurations
│   ├── support_chat/          # Chat app (handles chat views & logic)
│   │   ├── migrations/        # Database migrations
│   │   ├── templates/         # HTML templates
│   │   ├── static/            # Static files (CSS, JS)
│   │   ├── views.py           # Main views file
│   │   ├── urls.py            # URL routing
│   │   ├── models.py          # Database models
│   │   ├── forms.py           # Django forms (if any)
│   ├── manage.py              # Django's command-line utility
│── venv/                      # Virtual Environment
│── requirements.txt           # Required dependencies
│── README.md                  # Documentation (this file)
│── .gitignore                 # Files to ignore in Git
```

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/ai-support-chat.git
cd ai-support-chat
```

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv venv
```
> **Windows Users:**  
```bash
venv\Scripts\activate
```
> **Mac/Linux Users:**  
```bash
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Apply Migrations**
```bash
python manage.py migrate
```

### 5️⃣ **Create a Superuser (For Admin Access)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the admin account.

### 6️⃣ **Run the Server**
```bash
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser.

---

## 🔗 **Project Configuration**

### 🔹 **Setting Up `settings.py`**
Make sure `INSTALLED_APPS` includes:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'support_chat',  # Include the chat app
]
```

### 🔹 **Check `urls.py` in `ai_support`**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('support_chat.urls')),
]
```

### 🔹 **Check `urls.py` in `support_chat`**
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_page, name="chat_page"),
]
```

### 🔹 **Check `views.py` in `support_chat`**
```python
from django.shortcuts import render
from django.http import HttpResponse

def chat_page(request):
    return HttpResponse("Welcome to AI Support Chat!")
```

---

## 🔄 **Troubleshooting**

### ❌ **1. Module 'support_chat.views' has no attribute 'chat_page'**
✅ **Fix:**
1. Open `support_chat/views.py`
2. Ensure the function exists:
   ```python
   def chat_page(request):
       return HttpResponse("Welcome to AI Support Chat!")
   ```
3. Restart the server:
   ```bash
   python manage.py runserver
   ```

### ❌ **2. 'ModuleNotFoundError: No module named support_chat'**
✅ **Fix:**
1. Run:
   ```bash
   python manage.py shell
   ```
2. Check the import manually:
   ```python
   from support_chat.views import chat_page
   ```
   If an error appears, ensure `support_chat` is inside the Django project folder.

3. Delete cache files:
   ```bash
   rm -rf support_chat/__pycache__
   python manage.py runserver
   ```

### ❌ **3. 'Command not found: python'**
✅ **Fix:**  
Ensure Python is installed. Use:
```bash
python3 --version
```
If using **Python 3**, replace `python` with `python3` in all commands.

---


