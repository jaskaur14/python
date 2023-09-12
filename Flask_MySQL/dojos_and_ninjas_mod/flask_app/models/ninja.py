# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
# model the class after the friend table from our database
class Ninja:
    db = "d_and_n"
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.dojo_id = db_data['dojo_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo = None
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM ninjas
        ;"""
        ninjas_data = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for ninja in ninjas_data:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_one(cls, ninjas_id):
        query  = """
        SELECT * FROM ninjas WHERE id = %(id)s
        ;"""
        data = {'id': ninjas_id}
        results = connectToMySQL(cls.db).query_db(query, db_data)
        return cls(results[0])

    # CREATE model
    @classmethod
    def create_ninja(cls, ninja_data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)
        ;"""
        ninja_id = connectToMySQL(cls.db).query_db(query, ninja_data)
        return ninja_id


    # @classmethod
    # def save(cls, db_data):
    #     query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at ) 
    #     VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())
    #     ;"""
    #     return connectToMySQL('dojos_and_ninjas').query_db(query, db_data)