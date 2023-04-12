from fastapi import APIRouter
from fastapi.responses import JSONResponse
from mocks.clients import clients

client_router = APIRouter()
route_tag = 'clients'

@client_router.get('/clients', tags=[route_tag])
def get_clients():
  return JSONResponse(status_code = 200, content = clients)