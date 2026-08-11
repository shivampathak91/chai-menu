from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="ReDoc Test API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/redoc-test", response_class=HTMLResponse)
def redoc_test():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ReDoc Test</title>
    </head>
    <body>

        <redoc spec-url="/openapi.json"></redoc>

        <script src="https://unpkg.com/redoc@latest/bundles/redoc.standalone.js"></script>

    </body>
    </html>
    """