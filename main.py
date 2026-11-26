
from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware

from database import Base, engine, get_db
from models import ContactMessage


# Create FastAPI application
app = FastAPI()


# Enable sessions
app.add_middleware(
    SessionMiddleware,
    secret_key="change-this-to-a-long-random-secret-key"
)


# Create database tables automatically
Base.metadata.create_all(bind=engine)


# Static files
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Templates
templates = Jinja2Templates(directory="templates")


# Home route
@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# About route
@app.get("/about")
def about(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )


# Skills route
@app.get("/skills")
def skills(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="skills.html",
        context={}
    )


# Education route
@app.get("/education")
def education(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="education.html",
        context={}
    )


# Projects route
@app.get("/projects")
def projects(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="projects.html",
        context={}
    )


# Contact page - GET
@app.get("/contact")
def contact(request: Request):

    success_message = request.session.pop("success", None)
    error_message = request.session.pop("error", None)

    return templates.TemplateResponse(
        request=request,
        name="contact.html",
        context={
            "message": success_message,
            "error": error_message
        }
    )


# Contact form - POST
@app.post("/contact")
def submit_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
    db: Session = Depends(get_db)
):

    # Remove unnecessary spaces
    name = name.strip()
    email = email.strip()
    message = message.strip()

    # Validate submitted values
    if not name or not email or not message:

        request.session["error"] = "Please fill in all fields."

        return RedirectResponse(
            url="/contact",
            status_code=303
        )

    # Create a Python ORM object
    new_message = ContactMessage(
        name=name,
        email=email,
        message=message
    )

    # Add object to database session
    db.add(new_message)

    # Save object permanently in database
    db.commit()

    # Store success message in session
    request.session["success"] = (
        "Thank you! Your message has been saved successfully."
    )

    return RedirectResponse(
        url="/contact",
        status_code=303
    )


# Change theme using cookies
@app.post("/theme")
def change_theme(
    request: Request,
    theme: str = Form(...),
    next_page: str = Form("/")
):

    if theme not in ["light", "dark"]:
        theme = "light"

    if not next_page.startswith("/") or next_page.startswith("//"):
        next_page = "/"

    response = RedirectResponse(
        url=next_page,
        status_code=303
    )

    response.set_cookie(
        key="theme",
        value=theme,
        max_age=60 * 60 * 24 * 30,
        path="/",
        httponly=True,
        samesite="lax"
    )

    return response
