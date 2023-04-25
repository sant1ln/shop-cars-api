from fastapi import ApiRouter

cars_router = ApiRouter()

@cars_router.get('/cars')
def get_cars():
    pass
