import uvicorn
from fastapi import FastAPI

app = FastAPI(docs_url="/")


@app.get("/hola")
async def home():
    return "hola"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
