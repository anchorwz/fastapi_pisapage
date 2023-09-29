from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi import Request

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the path to the "static" directory for serving supporting files
static_dir = Path(__file__).parent / "static"

# Define the path to the "templates" directory for rendering HTML templates
templates = Jinja2Templates(directory="templates")

# Route to serve the index.html page
@app.get("/", response_class=HTMLResponse)
async def render_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to serve supporting files (e.g., task.tsk and file.table)
@app.get("/{filename}", response_class=FileResponse)
async def serve_static_files(filename: str):
    file_path = static_dir / filename

    if file_path.exists():
        return file_path
    else:
        return HTMLResponse(content=f"<h1>File not found: {filename}</h1>", status_code=404)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
