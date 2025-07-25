from flask_sqlalchemy import SQLAlchemy
from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, declarative_base
from datetime import datetime, timezone


#########################################################################################
#########################################################################################
#############                            TABLES                             #############
#############                       with SQL Alchemy                        #############
#############                         and classes                           #############
#########################################################################################
#########################################################################################
"""
TO-DOs:

[x] Create tables for STAR WARS Database Model:

4GEEKS version:
    [x] User
    [x] Favorite
    [x] People
    [x] Planet
    [x] Vehicle
"""

# class Base(DeclarativeBase):   # ------> This one DOES NOT work with how "app.py" is configured
#     pass

db = SQLAlchemy()
# class User(db.Model):

############################################
###########         USER         ###########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Atributes:
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
"""
class User(db.Model):
    __tablename__ = 'user'
    
    ### ATRIBUTES ###
    id:         Mapped[int]      = mapped_column(              primary_key=True)
    email:      Mapped[str]      = mapped_column( String(40),  unique=True,      nullable=False)
    username:   Mapped[str]      = mapped_column( String(40),  unique=True,      nullable=False)
    name:       Mapped[str]      = mapped_column( String(60),                    nullable=False)
    password:   Mapped[str]      = mapped_column( String(40),                    nullable=False)
    is_active:  Mapped[bool]     = mapped_column( Boolean(),   default=True,     nullable=False)
    creation:   Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)


    ### RELATIONS ###

    ### DE 4GEEKS
    # with Favorites --> Shows all the favorite things
    favorites: Mapped[List["Favorite"]] = relationship(
        back_populates="user",
        lazy="select"
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
    

############################################
##########         People         ##########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Atributes:
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

[] Create Relations
    [] ???
    [] ???

[x] Create serialization
"""
class People(db.Model):
    __tablename__ = 'people'

    ### ATRIBUTES ###

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
    url:         Mapped[str] = mapped_column( String(100),                   nullable=False)
    created:     Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)
    edited:      Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), onupdate=func.now())


    ### RELATIONS ###

    ### DE 4GEEKS
    # with Favorite --> ??????????????
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
    


############################################
##########         Planet         ##########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[] Create Atributes:
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
    [] ???
    [] ???

[] Create serialization
"""
class Planet(db.Model):
    __tablename__ = 'planet'

    ### ATRIBUTES ###
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
    edited:          Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), onupdate=func.now())


    ### RELATIONS ###

    # with Favorite --> ??????????????
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
    


############################################
##########         Vehicle         #########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[] Create Atributes:
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

[] Create Relations
    [] with Favorite

[] Create serialization
"""
class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    ### ATRIBUTES ###
    id:              Mapped[int] = mapped_column(              primary_key=True)
    name:            Mapped[str] = mapped_column( String(100), nullable=False)
    model:           Mapped[str] = mapped_column( String(100), nullable=False)
    vehicle_class:   Mapped[str] = mapped_column( String(100), nullable=False)
    manufacturer:    Mapped[str] = mapped_column( String(100), nullable=False)
    length:          Mapped[str] = mapped_column( String(100), nullable=False)
    cost_in_credits: Mapped[str] = mapped_column( String(100), nullable=False)
    crew:            Mapped[str] = mapped_column( String(20),  nullable=False)
    passengers:      Mapped[str] = mapped_column( String(20),  nullable=False)
    max_atmos_speed: Mapped[str] = mapped_column( String(100), nullable=False)
    cargo_capacity:  Mapped[str] = mapped_column( String(100), nullable=False)
    consumables:     Mapped[str] = mapped_column( String(100), nullable=False)
    url:             Mapped[str] = mapped_column( String(200), nullable=False)
    created:         Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), nullable=False)
    edited:          Mapped[datetime] = mapped_column( DateTime(timezone=True), default=func.now(), onupdate=func.now())
    

    ### RELATIONS ###

    # with Favorite --> ??????????????
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
            "cpassengers":      self.passengers,
            "max_atmos_speed":  self.max_atmos_speed,
            "cargo_capacity":   self.cargo_capacity,
            "consumables":      self.consumables,
            "url":              self.url,
            "created":          self.created.isoformat() if self.created else None,
            "edited":           self.edited.isoformat()  if self.edited  else None
        }
    

#######  -------------------------------------------------------------------------  ######


#################################################################
#################################################################
##################      Favorites HANDLING     ##################
#################################################################
#################################################################
"""
Diferentes versiones:
    [x] versión 4Geeks (1 sola tabla sin enum)
    [] versión Daniel (1 sola tabla CON enum)
    [] versión Varias tablas (x1 tabla por categoría)
"""
############################################
#########         Favorite         #########
#########          4Geeks          #########
############################################
"""
TO-DO's:

[x] Name the table with "__tablename__ ="

[x] Create Atributes:
    [x] 1. id
    [x] 2. user_id
    [x] 3. people_id
    [x] 4. vehicle_id
    [x] 5. planet_id

[x] Create Relations
    [x] with User
    [x] with People
    [x] with Vehicle
    [x] with Planet

[x] Create serialization
"""
class Favorite(db.Model):
    __tablename__ = 'favorite'
    
    ### ATRIBUTES ###

    id:         Mapped[int]           = mapped_column( primary_key=True)
    user_id:    Mapped[int]           = mapped_column( ForeignKey('user.id'),    nullable=False)
    people_id:  Mapped[Optional[int]] = mapped_column( ForeignKey('people.id'),  nullable=True)
    vehicle_id: Mapped[Optional[int]] = mapped_column( ForeignKey('vehicle.id'), nullable=True)
    planet_id:  Mapped[Optional[int]] = mapped_column( ForeignKey('planet.id'),  nullable=True)
    

    ### RELATIONS ###

    ### DE 4GEEKS

    # with User --> User that selected favorite
    user: Mapped["User"] = relationship(
        back_populates="favorites"
        )
    # with People --> ??????????????
    people: Mapped[Optional["People"]] = relationship(
        back_populates="favorites"
        )
    # with Vehicle --> ??????????????
    vehicle: Mapped[Optional["Vehicle"]] = relationship(
        back_populates="favorites"
        )
    # with Planet --> ??????????????
    planet: Mapped[Optional["Planet"]] = relationship(
        back_populates="favorites"
        )
    
    ### SERIALIZATION ###
    def serialize(self):
        return {
            "id":        self.id,
            "user_id":   self.user_id,
            "people_id": self.people_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id
        }
    
#######################

