from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routers.clients import client_router

#Init 
app = FastAPI()
app.title = "Auto shop api"
app.version = "0.0.1"

#Routes
app.include_router(client_router)

@app.get('/', tags=['Home'])
def home_test():
  return JSONResponse(status_code = 200, content = {"message":"Hello World"})