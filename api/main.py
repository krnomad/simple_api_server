import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

# main page
@app.get("/")
def pageIndex():
    return FileResponse('index.html')

@app.get("/data")
def pageData():
    return {'hello' : 1234}

class Model(BaseModel):
    name: str
    phone: int
    age: int

# TODO: connect DB
@app.post("/send")
def pageSend(data: Model):
    # TODO: get DB
    print(data)
    return f"${data} has been sent"


if __name__ == "__main__":
    # debug mode
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
