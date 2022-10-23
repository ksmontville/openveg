import models
import schema
import utils
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    'https://openveg-api.herokuapp.com/',
    'http://localhost:5173/',
    'https://localhost:8000',
    'https://localhost:3000',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    """Create a session of the SQlite database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
async def welcome():
    return {"message": "Welcome to the OpenVeg API!"}


@app.get('/restaurants/', response_model=list[schema.Restaurant], status_code=200)
def get_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), state: str | None = None,
                    city: str | None = None, zip: str | None = None, vegan: bool | None = False):
    restaurants = utils.get_restaurants(db, skip=skip, limit=limit, state=state, city=city, zip=zip, vegan=vegan)
    return restaurants


@app.post('/restaurants/', response_model=schema.Restaurant, status_code=201)
def create_restaurant(restaurant: schema.RestaurantCreate, db: Session = Depends(get_db)):
    existing_restaurants = utils.get_restaurant_by_name(db, restaurant_name=restaurant.name)
    if existing_restaurants:
        for some_restaurant in existing_restaurants:
            if some_restaurant.name == restaurant.name and some_restaurant.web == restaurant.web:
                raise HTTPException(status_code=422, detail="Restaurant already in database.")
    return utils.create_restaurant(db, restaurant)


@app.get('/restaurants/name/{restaurant_name}', response_model=list[schema.Restaurant], status_code=200)
def get_restaurant_by_name(restaurant_name: str, db: Session = Depends(get_db)):
    restaurants = utils.get_restaurant_by_name(db, restaurant_name=restaurant_name)
    if len(restaurants) == 0:
        raise HTTPException(status_code=404, detail="Restaurant is not in database.")
    return restaurants


@app.get('/restaurants/id/{restaurant_id}', response_model=schema.Restaurant, status_code=200)
def get_restaurant_by_id(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = utils.get_restaurant_by_id(db, restaurant_id=restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant is not in database.")
    return restaurant


@app.put('/restaurants/id/{restaurant_id}', response_model=schema.RestaurantPut, status_code=200)
def put_restaurant_by_id(restaurant_id: int, restaurant: schema.RestaurantPut, db: Session = Depends(get_db)):
    put_restaurant = utils.get_restaurant_by_id(db, restaurant_id=restaurant_id)
    if put_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant is not in database.")
    return utils.put_restaurant_by_id(db, restaurant_id, restaurant)


@app.delete('/restaurants/id/{restaurant_id}', status_code=200)
def delete_restaurant_by_id(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = utils.get_restaurant_by_id(db, restaurant_id=restaurant_id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant is not in database.")
    return utils.delete_restaurant_by_id(db, restaurant_id)

