from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash, session
from flask_app.models import sighting
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


class User:
    db = "sasquatch"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # update this
        self.things1 = []

    # READ methods

    @classmethod
    def get_all_users(cls):
        query = """
        SELECT * FROM users
        ;"""
        users_data = connectToMySQL(cls.db).query_db(query)
        users = []
        for users in users_data:
            users.append(cls(user))
        return users

    @classmethod
    def get_user_by_id(cls, user_id):
        user_id = {'user_id': user_id}
        query = """
        SELECT * FROM users
        WHERE id = %(id)s
        ;"""
        user_data = connectToMySQL(cls.db),query_db(query, user_id)
        if not user_data:
            return False
        return cls(user_data[0])

    @classmethod
    def get_user_by_email(cls, user_email):
        user_email = {'email': user_email}
        query = """
        SELECT * FROM users
        WHERE email = %(email)s
        ;"""
        user_em = connectToMySQL(cls.db).query_db(query, user_email)
        if user_em:
            return cls(user_em[0])
        return False

    # CREATE methods

    @classmethod
    def create_user(cls, user_info):
        if not cls.validate_user_data(user_info):
            return False
        user_info = user_info.copy()
        user_info['password'] = bcrypt.generate_password_hash(user_info['password'])
        query = """
        INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        ;"""
        user_id = connectToMySQL(cls.db).query_db(query, user_info)
        session['user_id'] = user_id
        session['user_name'] = f'{user_info["first_name"]} {user_info["last_name"]}'
        return user_id

    # LOGIN

    @staticmethod
    def login(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id 
                session['user_name'] = f'{this_user.first_name} {this_user.last_name}'
                return True
        flash('your login email or password was wrong')
        return False
    
    # VALIDATION
    @staticmethod
    def validate_user_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        if len(data['first_name']) < 2:
            flash("first name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("invalid email address.")
            is_valid = False
        if len(data['password']) < 8:
            flash("password must be at least 8 characters.")
            is_valid = False
        if User.get_user_by_email(data['email']):
            flash('that email is taken')
            is_valid = False
        if data['confirm_password'] != data['password']:
            flash("password must be the same.")
            is_valid = False
        return is_valid