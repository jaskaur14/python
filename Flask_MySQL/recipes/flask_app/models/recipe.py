from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash, session
from flask_app.models import user

class Recipe:
    db = "recipes"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.under30 = data['under30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def get_all_recipes(cls):
        query = """
        SELECT * FROM recipes
        JOIN users on recipes.user_id = users.id
        ;"""
        recipes_data = connectToMySQL(cls.db).query_db(query)
        recipes = []
        for row in recipes_data:
            this_recipe = cls(row)
            user_data = {
                "id":row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
            this_recipe.creator = user.User(user_data)
            recipes.append(this_recipe)
            print("recipes", recipes)
        return recipes

    @classmethod
    def get_by_id(cls, recipes_id):
        recipes_id = {'id': recipes_id}
        query = """
        SELECT * FROM recipes
        JOIN users on recipes.user_id = users.id
        WHERE recipes.id = %(id)s
        ;"""
        recipes_data = connectToMySQL(cls.db).query_db(query, recipes_id)
        if not recipes_data:
            return False

        recipes_data = recipes_data[0]
        this_recipe = cls(recipes_data)
        user_data = {
                "id" : recipes_data['id'],
                "first_name" : recipes_data['first_name'],
                "last_name" : recipes_data['last_name'],
                "email": recipes_data['email'],
                "password" : recipes_data['password'],
                "created_at" : recipes_data['created_at'],
                "updated_at" : recipes_data['updated_at']
        }
        this_recipe.creator = user.User(user_data)
        return this_recipe

    # CREATE
    @classmethod
    def create_recipe(cls, recipe_data):
        if not cls.validate_recipe_data(recipe_data):
            return False
        query = """
        INSERT INTO recipes (name, under30, description, instructions, date_made, user_id)
        VALUES (%(name)s, %(under30)s, %(description)s, %(instructions)s, %(date_made)s, %(user_id)s)
        ;"""
        recipe_id = connectToMySQL(cls.db).query_db(query, recipe_data)
        print(recipe_id)
        return recipe_id

    @classmethod
    def update_recipe(cls, recipe_data):
        if not cls.validate_recipe_data(recipe_data):
            return False
        query = """
        UPDATE recipes
        SET name=%(name)s, under30=%(under30)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, user_id=%(user_id)s
        WHERE id= %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, recipe_data)
        print(recipe_data)
        return True

    @classmethod
    def delete_recipe_by_id(cls, id):
        data = {'id' : id}
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s
        ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return

    @staticmethod
    def validate_recipe_data(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("recipe name must be at least 3 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("description must be at least 3 characters")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("instructions must be at least 3 characters.")
            is_valid = False
        if data['date_made'] == '':
            flash("please input a date")
            is_valid = False
        if 'under30' not in data:
            flash("input cook time.")
            is_valid = False
        return is_valid
