
from flask_sqlalchemy import SQLAlchemy
from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declarative_base
from datetime import datetime, timezone


#########################################################################################
#########################################################################################
#############                            TABLES                             #############
#############                        Star Wars Blog                         #############
#############                       with SQL Alchemy                        #############
#############                         and classes                           #############
#########################################################################################
#########################################################################################
"""
TO-DOs:

[x] Create tables for STAR WARS Database Model:

Project delivery version:
    [x] User
    [x] Favorite
    [x] People
    [x] Planet
    [x] Vehicle
"""

# class Base(DeclarativeBase):   # ------> This one DOES NOT work
#     pass

db = SQLAlchemy()
# class User(db.Model):

############################################
###########         USER         ###########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Attributes:
    [x] id
    [x] email
    [x] username
    [x] name
    [x] password
    [x] is_active
    [x] creation

[x] Create Relations
    [x] with Favorite

[x] Create serialization

[x] Create "__repr__" method
"""
class User(db.Model):
    __tablename__ = 'user'
    
    ### ATTRIBUTES ###
    id:         Mapped[int]      = mapped_column(              primary_key=True)
    email:      Mapped[str]      = mapped_column( String(40),  unique=True,      nullable=False)
    username:   Mapped[str]      = mapped_column( String(40),  unique=True,      nullable=False)
    name:       Mapped[str]      = mapped_column( String(60),                    nullable=False)
    password:   Mapped[str]      = mapped_column( String(255),                   nullable=False)
    is_active:  Mapped[bool]     = mapped_column( Boolean(),   default=True,     nullable=False)
    creation:   Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)


    ### RELATIONS ###

    # One-to-Many relationship with Favorites --> shows all items this user has favorited
    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="user",
        lazy="select",
        cascade="all, delete-orphan"  # Delete favorites when user is deleted
        )
    

    ### SERIALIZATION ###
    def serialize(self):
        return {
            "id":          self.id,
            "is_active":   self.is_active,
            "email":       self.email,
            "username":    self.username,
            "name":        self.name,
            "favorites":   [favorite.serialize() for favorite in self.favorites]
            # do not serialize the password, its a security breach !!!
        }
    
    ### __repr__ METHOD ###

    def __repr__(self):
        return f"<User {self.id} - {self.username} - {self.email} - {self.name}>"

############################################
##########         People         ##########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Attributes:
    [x] id
    [x] name
    [x] birth_year
    [x] eye_color
    [x] gender
    [x] hair_color
    [x] height
    [x] mass
    [x] skin_color
    [x] homeworld
    [x] url
    [x] created
    [x] edited

[x] Create Relations
    [x] with Favorite

[x] Create serialization

[x] Create "__repr__" method
"""
class People(db.Model):
    __tablename__ = 'people'

    ### ATTRIBUTES ###

    id:          Mapped[int] = mapped_column(              primary_key=True)
    name:        Mapped[str] = mapped_column( String(100),                   nullable=False)
    birth_year:  Mapped[str] = mapped_column( String(100),                   nullable=False)
    eye_color:   Mapped[str] = mapped_column( String(100),                   nullable=False)
    gender:      Mapped[str] = mapped_column( String(100),                   nullable=False)
    hair_color:  Mapped[str] = mapped_column( String(100),                   nullable=False)
    height:      Mapped[str] = mapped_column( String(20),                    nullable=False)
    mass:        Mapped[str] = mapped_column( String(40),                    nullable=False)
    skin_color:  Mapped[str] = mapped_column( String(20),                    nullable=False)
    homeworld:   Mapped[str] = mapped_column( String(40),                    nullable=False)
    url:         Mapped[str] = mapped_column( String(100), unique=True,      nullable=False)
    created:     Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)
    edited:      Mapped[Optional[datetime]] = mapped_column( DateTime(timezone=True), default=func.now(), onupdate=func.now())


    ### RELATIONS ###

    # One-to-many relationship with Favorite - shows which users have favorited this person
    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="people",
        lazy="select"
        )

    ### SERIALIZATION ###
    def serialize(self):
        return {
            "id":          self.id,
            "name":        self.name,
            "birth_year":  self.birth_year,
            "eye_color":   self.eye_color,
            "gender":      self.gender,
            "hair_color":  self.hair_color,
            "height":      self.height,
            "mass":        self.mass,
            "skin_color":  self.skin_color,
            "homeworld":   self.homeworld,
            "url":         self.url,
            "created":     self.created.isoformat()  if self.created else None,
            "edited":      self.edited.isoformat()   if self.edited  else None
        }
    

    ### __repr__ METHOD ###

    def __repr__(self): 
        return f"<People {self.id} - {self.name}>"

############################################
##########         Planet         ##########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Attributes:
    [x] id
    [x] name
    [x] diameter
    [x] rotation_period
    [x] orbital_period
    [x] gravity
    [x] population
    [x] climate
    [x] terrain
    [x] surface_water
    [x] created
    [x] edited

[] Create Relations
    [] with Favorite

[] Create serialization

[] Create "__repr__" method
"""
class Planet(db.Model):
    __tablename__ = 'planet'

    ### ATTRIBUTES ###
    id:              Mapped[int] = mapped_column(              primary_key=True)
    name:            Mapped[str] = mapped_column( String(100),                   nullable=False)
    diameter:        Mapped[str] = mapped_column( String(100),                   nullable=False)
    rotation_period: Mapped[str] = mapped_column( String(100),                   nullable=False)
    orbital_period:  Mapped[str] = mapped_column( String(100),                   nullable=False)
    gravity:         Mapped[str] = mapped_column( String(100),                   nullable=False)
    population:      Mapped[str] = mapped_column( String(100),                   nullable=False)
    climate:         Mapped[str] = mapped_column( String(100),                   nullable=False)
    terrain:         Mapped[str] = mapped_column( String(100),                   nullable=False)
    surface_water:   Mapped[str] = mapped_column( String(100),                   nullable=False)
    created:         Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)
    edited:          Mapped[Optional[datetime]] = mapped_column( DateTime(timezone=True), default=func.now(), onupdate=func.now())


    ### RELATIONS ###

    # One-to-many relationship with Favorite - shows which users have favorited this planet
    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="planet",
        lazy="select"
        )


    ### SERIALIZATION ###
    def serialize(self):
        return {
            "id":              self.id,
            "name":            self.name,
            "diameter":        self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period":  self.orbital_period,
            "gravity":         self.gravity,
            "population":      self.population,
            "climate":         self.climate,
            "terrain":         self.terrain,
            "surface_water":   self.surface_water,
            "created":         self.created.isoformat()  if self.created else None,
            "edited":          self.edited.isoformat()   if self.edited  else None
        }
    

    ### __repr__ METHOD ###

    def __repr__(self):
        return f"<Planet {self.id} - {self.name}>"


############################################
##########         Vehicle         #########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Attributes:
    [x] id
    [x] name
    [x] model
    [x] vehicle_class
    [x] manufacturer
    [x] length
    [x] cost_in_credits
    [x] crew
    [x] passengers
    [x] max_atmos_speed
    [x] cargo_capacity
    [x] consumables
    [x] url
    [x] created
    [x] edited

[x] Create Relations
    [x] with Favorite

[x] Create serialization

[x] Create "__repr__" method
"""
class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    ### ATTRIBUTES ###
    id:              Mapped[int] = mapped_column(              primary_key=True)
    name:            Mapped[str] = mapped_column( String(100),                    nullable=False)
    model:           Mapped[str] = mapped_column( String(100),                    nullable=False)
    vehicle_class:   Mapped[str] = mapped_column( String(100),                    nullable=False)
    manufacturer:    Mapped[str] = mapped_column( String(100),                    nullable=False)
    length:          Mapped[str] = mapped_column( String(100),                    nullable=False)
    cost_in_credits: Mapped[str] = mapped_column( String(100),                    nullable=False)
    crew:            Mapped[str] = mapped_column( String(20),                     nullable=False)
    passengers:      Mapped[str] = mapped_column( String(20),                     nullable=False)
    max_atmos_speed: Mapped[str] = mapped_column( String(100),                    nullable=False)
    cargo_capacity:  Mapped[str] = mapped_column( String(100),                    nullable=False)
    consumables:     Mapped[str] = mapped_column( String(100),                    nullable=False)
    url:             Mapped[str] = mapped_column( String(200), unique=True,       nullable=False)
    created:         Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)
    edited:          Mapped[Optional[datetime]] = mapped_column( DateTime(timezone=True), default=func.now(), onupdate=func.now())
    

    ### RELATIONS ###

    # One-to-many relationship with Favorite - shows which users have favorited this vehicle
    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="vehicle",
        lazy="select"
        )

    ### SERIALIZATION ###
    def serialize(self):
        return {
            "id":               self.id,
            "name":             self.name,
            "model":            self.model,
            "vehicle_class":    self.vehicle_class,
            "manufacturer":     self.manufacturer,
            "length":           self.length,
            "cost_in_credits":  self.cost_in_credits,
            "crew":             self.crew,
            "passengers":       self.passengers,
            "max_atmos_speed":  self.max_atmos_speed,
            "cargo_capacity":   self.cargo_capacity,
            "consumables":      self.consumables,
            "url":              self.url,
            "created":          self.created.isoformat() if self.created else None,
            "edited":           self.edited.isoformat()  if self.edited  else None
        }


    ### __repr__ METHOD ###

    def __repr__(self):
        return f"<Vehicle {self.id} - {self.name} - {self.model} - {self.vehicle_class}>"
    

#######  -------------------------------------------------------------------------  ######


#################################################################
#################################################################
##################      Favorites HANDLING     ##################
##################           ONE table         ##################
##################         with nullables      ##################
#################################################################
#################################################################
"""
Different Versions:

    1. [x] ONLY one Favorite Table  ---    Nullable entries -- NO   Enum

    2. []  ONLY one Favorite Table  --- NO Nullable entries -- WITH Enum

    3. []  ONLY one Favorite Table  --- NO Nullable entries -- NO   Enum -- Many to Many relationship

    4. []  MULTIPLE Favorite Tables --- NO Nullable entries -- NO   Enum
          (x1 table per category)
"""
############################################
#########         Favorite         #########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Attributes:
    [x] id
    [x] user_id
    [x] people_id
    [x] vehicle_id
    [x] planet_id

[x] Create Relations
    [x] with User
    [x] with People
    [x] with Vehicle
    [x] with Planet

[x] Create serialization

[x] Create "__repr__" method
"""
class Favorite(db.Model):
    __tablename__ = 'favorite'
    
    ### ATTRIBUTES ###

    id:         Mapped[int]           = mapped_column( primary_key=True)

    user_id:    Mapped[int]           = mapped_column( ForeignKey('user.id'),    nullable=False)
    people_id:  Mapped[Optional[int]] = mapped_column( ForeignKey('people.id'),  nullable=True)
    vehicle_id: Mapped[Optional[int]] = mapped_column( ForeignKey('vehicle.id'), nullable=True)
    planet_id:  Mapped[Optional[int]] = mapped_column( ForeignKey('planet.id'),  nullable=True)
    

    ### RELATIONS ###

    ### DE 4GEEKS

    # Many-to-one relationship with User - the user who created this favorite
    user: Mapped["User"] = relationship(
        back_populates="favorites"
        )
    
    # Many-to-one relationship with People - the person being favorited (if applicable)
    people: Mapped[Optional["People"]] = relationship(
        back_populates="favorites"
        )
    
    # Many-to-one relationship with Vehicle - the vehicle being favorited (if applicable)
    vehicle: Mapped[Optional["Vehicle"]] = relationship(
        back_populates="favorites"
        )
    
    # Many-to-one relationship with Planet - the planet being favorited (if applicable)
    planet: Mapped[Optional["Planet"]] = relationship(
        back_populates="favorites"
        )
    
    ### SERIALIZATION ###
    def serialize(self):
        favorite_data = {
            "id": self.id,
            "user_id": self.user_id
        }

        if self.people:
            favorite_data["favorite_type"] = "people"
            favorite_data["people_id"] = self.people_id
            favorite_data["people"] = self.people.serialize()

        elif self.vehicle:
            favorite_data["favorite_type"] = "vehicle"
            favorite_data["vehicle_id"] = self.vehicle_id
            favorite_data["vehicle"] = self.vehicle.serialize() 

        elif self.planet:
            favorite_data["favorite_type"] = "planet"
            favorite_data["planet_id"] = self.planet_id
            favorite_data["planet"] = self.planet.serialize()
            
        return favorite_data


    ### __repr__ METHOD ###

    def __repr__(self):
        if self.people_id:
            return f'<Favorite User:{self.user_id} -> People:{self.people_id}>'
        elif self.vehicle_id:
            return f'<Favorite User:{self.user_id} -> Vehicle:{self.vehicle_id}>'
        elif self.planet_id:
            return f'<Favorite User:{self.user_id} -> Planet:{self.planet_id}>'
        else:
            return f'<Favorite User:{self.user_id} -> Unknown>'
        
########################################################################################################



