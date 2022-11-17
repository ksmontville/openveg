from pydantic import BaseModel


class RestaurantBase(BaseModel):
    """A schema for handling Restaurant class data."""
    name: str
    description: str | None = None
    vegan: bool | None = None
    web: str = None
    email: str = None
    phone: str = None
    address: str | None = None
    state: str | None = None
    city: str | None = None
    zip: str | None = None


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantPut(RestaurantBase):
    id: int


class Restaurant(RestaurantBase):
    """The API will return this class to the user."""
    id: int

    class Config:
        orm_mode = True
