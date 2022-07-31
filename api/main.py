import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import FileResponse
from typing import Optional

app = FastAPI()

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

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



class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return fake_db.get(item_id, None)

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")

    fake_db[item.id] = item
    return item

if __name__ == "__main__":
    # debug mode
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
