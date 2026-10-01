from fastapi import FastAPI

# uvicorn main:app --reload

app = FastAPI()

@app.post("/news")
def news():
    return {'news': 'today we created this news'}