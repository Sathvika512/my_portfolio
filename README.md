
# 🌐 Personal Portfolio Website

A personal portfolio website developed using **Python and FastAPI** to showcase my profile, technical skills, education, and projects.

The application also includes a contact form with database integration and a light/dark theme feature using cookies.

## 🚀 Technologies Used

- **Programming Language:** Python
- **Backend Framework:** FastAPI
- **Frontend:** HTML, CSS
- **Template Engine:** Jinja2
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Session Management:** Starlette SessionMiddleware

## ✨ Features

### 1. Multiple Portfolio Pages
- Home
- About
- Skills
- Education
- Projects
- Contact

### 2. Dynamic Template Rendering
- Jinja2 template rendering
- Template inheritance
- Reusable base layout
- Common navigation across pages

### 3. Light and Dark Theme
- Light mode and dark mode
- Theme preference stored using cookies
- Theme preference maintained across different pages
- No JavaScript used for theme switching

### 4. Contact Form
- Collects name, email, and message
- Validates submitted form data
- Stores contact messages in SQLite
- Uses SQLAlchemy ORM for database operations

### 5. Session Management
- Uses sessions to display success and error messages
- Flash messages after contact form submission

## 📂 Project Structure

```text
my_portfolio/
│
├── routers/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── profile.jpg
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── skills.html
│   ├── education.html
│   ├── projects.html
│   └── contact.html
│
├── database.py
├── models.py
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Sathvika512/my_portfolio.git
```

### Step 2: Navigate to the Project Folder

```bash
cd my_portfolio
```

### Step 3: Create a Virtual Environment

```bash
python -m venv env
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\env\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python -m uvicorn main:app --reload
```

### Step 7: Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## 🗄️ Database

This project uses SQLite as its database and SQLAlchemy as the ORM.

Contact form submissions are stored in the database through the `ContactMessage` model.

The database tables are created automatically when the application starts.

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Building web applications using FastAPI
- Creating and managing application routes
- Working with Jinja2 templates and template inheritance
- Understanding cookies and session management
- Implementing SQLAlchemy ORM
- Performing database operations
- Connecting frontend forms with backend functionality
- Organizing a Python web application

## 👩‍💻 Developer

**Sathvika**

Full Stack Python Developer

## 🔗 Repository

[GitHub - Personal Portfolio Website](https://github.com/Sathvika512/my_portfolio)

---

⭐ If you find this project useful, feel free to explore the repository!
