from fastapi import FastAPI
app = FastAPI() 


@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "Us"}
@app.get("/contact")
def contact():
    return {"message": "Contact Us"}