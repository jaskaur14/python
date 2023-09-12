from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User:
    # db= 'log_and_reg'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# READ
    @classmethod
    def get_all_users(cls):
        query = """
        SELECT * 
        FROM users
        ;"""
        users_from_db = connectToMySQL('log_and_reg').query_db(query)
        all_users = []
        for u in users_from_db:
            all_users.append(cls(u))
        return all_users

    @classmethod
    def get_user_by_email(cls, email):
        data = {'email' : email}
        query = """
        SELECT * 
        FROM users
        WHERE email = %(email)s
        ;"""
        user_data = connectToMySQL('log_and_reg').query_db(query, data)
        if user_data:
            return cls(user_data[0])
        return False

# CREATE
    @classmethod
    def create_user(cls, user_info):
        if not cls.validate_user_data(user_info):
            return False
        user_info = user_info.copy()
        user_info['password'] = bcrypt.generate_password_hash(user_info['password'])
        query = """
        INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) 
        VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())
        ;"""
        user_id = connectToMySQL('log_and_reg').query_db(query,user_info)
        session['user_id'] = user_id
        session['user_name'] = f'{user_info["first_name"]}'
        return user_id

# LOGIN
    @staticmethod
    def login(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                session['user_name'] = f'{this_user.first_name}'
                return True
            flash('Your login email or password was wrong.')
            return False

# HELPER METHODS
    @staticmethod
    def validate_user_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(data['first_name']) < 2 :
            flash('first name must contain more than 2 letters!')
            is_valid = False
        if len(data['last_name']) < 2 :
            flash('last name must contain more than 2 letters!')
            is_valid = False    
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(data['password']) < 8:
            flash('password must be 8 characters long!')
            is_valid = False
        if User.get_user_by_email(data['email']):
            flash('That email is taken')
            is_valid = False
        return is_valid

    # @staticmethod
    # def parse_user_data(data):
    #     parsed_data = {
    #         'first_name': data['first_name'],
    #         'last_name': data['last_name'],
    #         'email': data['email'],
    #         'password': bcrypt.generate_password_hash(data['password'])
    #     }
    #     print('!!!!!!!!!', parsed_data)
    #     return (parsed_data)