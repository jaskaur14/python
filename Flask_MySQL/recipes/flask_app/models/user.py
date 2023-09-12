from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash, session
from flask_app.models import recipe
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class User:
    db = "recipes"
    def __init__(self, data):
        # if isinstance(data, list):
        #     data = data[0]
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []

    # READ
    @classmethod
    def get_all_users(cls):
        query = """
        SELECT * FROM users
        ;"""
        users_data = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in users_data:
            users.append(cls(user))
        return users
    
    @classmethod
    def get_user_by_id(cls, user_id):
        user_id = {'user_id' : user_id}
        query = """
        SELECT * FROM users WHERE id = %(id)s
        ;"""
        user_data = connectToMySQL(cls.db).query_db(query, user_id)
        if not user_data:
            return False
        print("!!!!!!!!!!!!!" , user_id)
        return cls(user_data[0])

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
        session['user_name'] = f'{user_info["first_name"]}'
        return user_id

    @classmethod
    def get_user_by_email(cls, user_email):
        user_email = {'email' : user_email}
        query = """
        SELECT * FROM users
        WHERE email = %(email)s
        ;"""
        user_em = connectToMySQL(cls.db).query_db(query, user_email)
        if user_em:
            return cls(user_em[0])
        return False


    # LOGIN
    @staticmethod
    def login(data):
        this_user = User.get_user_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                # this_user.password,
                session['user_id'] = this_user.id
                session['user_name'] = f'{this_user.first_name}'
                print(session)
                return True
        flash ('your login email or password was wrong')
        print(data)
        return False

    @staticmethod
    def validate_user_data(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        if len(data['first_name']) < 3:
            flash("first name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("invalid email address.")
            is_valid = False
        if len(data['password']) < 3:
            flash("password must be at least 3 characters.")
            is_valid = False
        if User.get_user_by_email(data['email']):
            flash('that email is taken')
            is_valid = False
        if data['confirm_password'] != data['password']:
            flash("password must be the same.")
            is_valid = False
        return is_valid


    # @classmethod
    # def get_user_by_id_with_recipes(cls, user_id):
    #     data = {'id': user_id}
    #     query = """
    #     SELECT * FROM users
    #     LEFT JOIN recipes
    #     ON users.id = recipes.user_id
    #     WHERE users.id = %(id)s
    #     ;"""
    #     user_data = connectToMySQL(cls.db).query_db(query, data)
    #     this_user = cls(user_data[0])
    #     for row in user_data:
    #         recipe_data = {
    #             "id" == row['recipes.id'],
    #             "user_id" == row['user_id'],
    #             "name" == row['name'],
    #             "under30" == row['under30'],
    #             "description"== row['description'],
    #             "instructions" == row['instructions'],
    #             "date_made" == row['date_made'],
    #             "created_at" == row['recipes.created_at'],
    #             "updated_at" == row['recipes.updated_at']
    #         }
    #         this_user.recipes.append(recipe.Recipe(row))
    #         print("this_user", this_user)
    #         return this_user