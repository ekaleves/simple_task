from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

from app.routes import router
from app.database import init_db

app = FastAPI()

# Serve static files from app/static
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Route to serve the favicon
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return RedirectResponse(url="/static/favicon.ico")


init_db()
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to SimpleTask API!"}
