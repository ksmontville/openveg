import models
import schema
from sqlalchemy.orm import Session


# Helper method for updating restaurants
def _update_restaurant(old_restaurant, new_restaurant):
    old_restaurant.name = new_restaurant.name
    old_restaurant.description = new_restaurant.description
    old_restaurant.vegan = new_restaurant.vegan
    old_restaurant.web = new_restaurant.web
    old_restaurant.email = new_restaurant.email
    old_restaurant.phone = new_restaurant.phone
    old_restaurant.address = new_restaurant.address
    old_restaurant.state = new_restaurant.state
    old_restaurant.city = new_restaurant.city
    old_restaurant.zip = new_restaurant.zip


def get_restaurants(db: Session, skip: int = 0, limit: int = 100,
                    state: str | None = None, city: str | None = None, zip: str | None = None,
                    vegan: bool | None = False):

    if state and city:
        if vegan:
            return db.query(models.Restaurant).filter(
                models.Restaurant.state == state, models.Restaurant.city == city, models.Restaurant.vegan
            ).offset(skip).limit(limit).all()

        return db.query(models.Restaurant).filter(
            models.Restaurant.state == state, models.Restaurant.city == city).offset(skip).limit(limit).all()

    elif zip:
        if vegan:
            return db.query(models.Restaurant).filter(
                models.Restaurant.zip == zip, models.Restaurant.vegan).offset(skip).limit(limit).all()

        return db.query(models.Restaurant).filter(
            models.Restaurant.zip == zip).offset(skip).limit(limit).all()

    elif vegan:
        return db.query(models.Restaurant).filter(models.Restaurant.vegan).offset(skip).limit(limit).all()

    return db.query(models.Restaurant).offset(skip).limit(limit).all()


def create_restaurant(db: Session, restaurant: schema.RestaurantCreate):
    new_restaurant = models.Restaurant(
        name=restaurant.name,
        description=restaurant.description,
        vegan=restaurant.vegan,
        web=restaurant.web,
        email=restaurant.email,
        phone=restaurant.phone,
        address=restaurant.address,
        state=restaurant.state,
        city=restaurant.city,
        zip=restaurant.zip
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return new_restaurant


def get_restaurant_by_name(db: Session, restaurant_name: str):
    return db.query(models.Restaurant).filter(models.Restaurant.name == restaurant_name).all()


def get_restaurant_by_id(db: Session, restaurant_id: int):
    return db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()


def put_restaurant_by_id(db: Session, restaurant_id: int, restaurant: schema.RestaurantPut):
    old_restaurant = db.query(models.Restaurant).get(restaurant_id)
    _update_restaurant(old_restaurant=old_restaurant, new_restaurant=restaurant)
    db.commit()
    return restaurant


def delete_restaurant_by_id(db: Session, restaurant_id: int):
    restaurant = db.query(models.Restaurant).get(restaurant_id)
    db.delete(restaurant)
    db.commit()
    return {"message": "Restaurant successfully deleted."}
