import datetime

from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('photos.sqlite')

class User(UserMixin, Model):
    username        = CharField(unique=True)
    email           = CharField(unique=True)
    password        = CharField()
    verify_password = CharField()

    class Meta:
        database = DATABASE
    
    @classmethod
    def create_user(cls, username, email, password, verify_password, **kwargs):
        email = email.lower()
        try:
            cls.select().where(
                (cls.email==email)
            ).get()
        except cls.DoesNotExist:
            user = cls(username = username,email=email)
            user.password = (password)
            user.verify_password = (verify_password)
            user.save()
            return user
        else:
            return "user with that email exists"

class Photo(Model):
    title = CharField()
    category = CharField()
    url = CharField()
    description = CharField()
    camera = CharField()
    category = CharField()
    created_by = ForeignKeyField(User, related_name='photos')

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect() 
    DATABASE.create_tables([User], safe=True)
    DATABASE.create_tables([Photo], safe=True)
    DATABASE.close()