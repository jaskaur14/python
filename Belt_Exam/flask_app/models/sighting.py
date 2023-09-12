from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash, session
from flask_app.models import user

class Sighting:
    db = "sasquatch"
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.date_seen = data['date_seen']
        self.what_happened = data['what_happened']
        self.num_of_sasquatches = data['num_of_sasquatches']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self. creator = None

    # READ
    @classmethod
    def get_all_sightings(cls):
        query = """
        SELECT * FROM sightings
        JOIN users on sightings.user_id = users.id
        ;"""
        sightings_data = connectToMySQL(cls.db).query_db(query)
        sightings = []
        for row in sightings_data:
            this_sighting = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at'],
            }
            this_sighting.creator = user.User(user_data)
            sightings.append(this_sighting)
            print("sightings", sightings)
        return sightings

    @classmethod
    def get_sighting_by_id(cls, sightings_id):
        sightings_id = {'id': sightings_id}
        query = """
        SELECT * FROM sightings
        JOIN users on sightings.user_id = users.id
        WHERE sightings.id = %(id)s
        ;"""
        sightings_data = connectToMySQL(cls.db).query_db(query, sightings_id)
        if not sightings_data:
            return False

        sightings_data = sightings_data[0]
        this_sighting = cls(sightings_data)
        user_data = {
            "id": sightings_data['id'],
            "first_name": sightings_data['first_name'],
            "last_name": sightings_data['last_name'],
            "email": sightings_data['email'],
            "password":  sightings_data['password'],
            "created_at": sightings_data['created_at'],
            "updated_at": sightings_data['updated_at'],
        }
        this_sighting.creator = user.User(user_data)
        return this_sighting

    # CREATE, UPDATE, DELETE
    @classmethod
    def create_sighting(cls, sighting_data):
        if not cls.validate_sighting_data(sighting_data):
            return False
        query = """
        INSERT INTO sightings (location, date_seen, what_happened, num_of_sasquatches, user_id)
        VALUES (%(location)s, %(date_seen)s, %(what_happened)s, %(num_of_sasquatches)s, %(user_id)s)
        ;"""
        sighting_id = connectToMySQL(cls.db).query_db(query, sighting_data)
        return sighting_id

    @classmethod
    def update_sighting(cls, sighting_data):
        if not cls.validate_sighting_data(sighting_data):
            return False
        query = """
        UPDATE sightings
        SET location=%(location)s, date_seen=%(date_seen)s, what_happened=%(what_happened)s, num_of_sasquatches=%(num_of_sasquatches)s, user_id=%(user_id)s
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, sighting_data)
        return True

    @classmethod
    def delete_sighting_by_id(cls, id):
        data = {'id': id}
        query = """
        DELETE FROM sightings
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return

    # VALIDATIONS

    @staticmethod
    def validate_sighting_data(data):
        is_valid = True
        if len(data['location']) < 3:
            flash ('location must be 3 characters long')
            is_valid = False
        if data['date_seen'] == '':
            flash ('please input a date')
            is_valid = False
        if len(data['what_happened']) < 3:
            flash ('sighting description must be 3 characters long')
            is_valid = False
        if data['num_of_sasquatches'] == '':
            flash ('please input number higher or equal to 1')
            is_valid = False
        return is_valid
            
