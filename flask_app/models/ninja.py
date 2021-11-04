from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja:
    def __init__( self , data ):
        print (data)
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        print('Hello')
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s,NOW(), NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db( query, data )


    @classmethod
    def getall(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas= []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas


    @classmethod
    def getdojo(cls, dojos_id):
        print (dojos_id)
        query = "SELECT * FROM ninjas Where dojos_id = "+str(dojos_id)+';'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        print(results)
        ninjas= []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas