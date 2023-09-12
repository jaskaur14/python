# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
from flask_app.models import ninja
# model the class after the friend table from our database
class Dojo:
    db = "d_and_n"
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []
    # Now we use class methods to query our database

    @classmethod
    def get_all_dojos(cls):
        query = """
        SELECT * FROM dojos
        ;"""
        dojos_data = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in dojos_data:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_dojo_by_id(cls, dojo_id):
        data = {'id': dojo_id}
        query  = """
        SELECT * FROM dojos WHERE id = %(id)s
        ;"""
        dojo_data = connectToMySQL(cls.db).query_db(query, data)
        return cls(dojo_data[0])

    # CREATE model
    @classmethod
    def create_dojo(cls, dojo_info):
        query = """
        INSERT INTO dojos (name) VALUES (%(name)s)
        ;"""
        dojo_id = connectToMySQL(cls.db).query_db(query, dojo_info)
        return dojo_id

    @classmethod
    def get_dojo_by_id_with_ninjas(cls, dojo_id):
        db_data= {'id': dojo_id}
        query = """
        SELECT * 
        FROM dojos 
        LEFT JOIN ninjas 
        ON ninjas.dojo_id = dojos.id 
        WHERE dojos.id = %(id)s
        ;"""
        dojo_data = connectToMySQL(cls.db).query_db(query, db_data) 
        this_dojo = cls(dojo_data[0])
        for row_from_db in dojo_data:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            this_dojo.ninjas.append(ninja.Ninja(ninja_data))
        print("this_dojo", this_dojo)
        return this_dojo        
