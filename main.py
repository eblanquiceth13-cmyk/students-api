from fastapi import fastAPI
from config import APP_VERSION

app = fastAPI(title="students-api", version=APP_VERSION)

@app.get("/health")
def health():
    return {"status": "ok"}