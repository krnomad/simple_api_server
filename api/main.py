from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse

# main page
@app.get("/")
def 작명():
  return FileResponse('index.html')

@app.get("/data")
def 작명2():
  return {'hello' : 1234}

from pydantic import BaseModel
class Model(BaseModel):
  name: str
  phone: int

# DB접속하는 로직
@app.post("/send")
def 작명4(data: Model):
  # DB에서 꺼내는 로직
  print(data)
  return f"${data} 전송완료"

#@app.post("/send2")
# async def 작명5(data: Model):
#   await ?
#   print(data)
#   return '전송완료'
