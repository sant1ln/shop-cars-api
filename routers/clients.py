from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from mocks.clients import clients

client_router = APIRouter()
route_tag = 'clients'

@client_router.get('/clients', tags=[route_tag])
def get_clients():
  return JSONResponse(status_code = 200, content = clients)

@client_router.get('/clients/{id}', tags=[route_tag])
def get_client(id : int = Path(ge=1, le=2000)):
  for item in clients:
    print(type(id))
    print(type(item["id"]))
    if item["id"] == id:
      return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

@client_router.post('/clients', tags=[route_tag])
def create_client(client):
  pass