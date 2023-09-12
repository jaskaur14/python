from flask_app.config.mysqlconnection import connectToMySQL
#we make the class look like the table in the database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #self passes data from db
    # the getall is used to get all the data from the database and put into instances of our class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # now we're calling on the connectToMySQL function with the users schema
        results = connectToMySQL('users').query_db(query)
        # now creating an empty list to append our instances of users
        users = []
        # now iterating over the database results and creating instances of users with cls
        for s in results:
            users.append(cls(s))
        return users
            
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        # creates row in the database with all our information in it; must use prepared statement because this query includes variables
        return connectToMySQL('users').query_db( query, data )