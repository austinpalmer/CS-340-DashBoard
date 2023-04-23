from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import json_util

class AnimalShelter(object):
    """A class to implement create, read, update, delete with mongoDB"""

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:48517/AAC' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']

    def create(self, data):
        """A method to create new data"""
        if data is not None:
            # If there is data, add to db
            insert = self.database.animals.insert(data)
            if insert != 0:
                # Return true if data is changed
                return True
            else:
                # Data was not changed
                return False      
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    def read(self, searchVal= None):
        """A method to read data based on searchVal"""
        if searchVal:
            # Search file for searchVal
            data = self.database.animals.find(searchVal, {"_id": False})
        else:
            # Read entire file
            data = self.database.animals.find({}, {"_id":False})

        return data
    
    def update(self, searchVal, updateVal):
        """A method to update data"""
        if searchVal and updateVal:
            # Search file for searchVal         
            result = self.database.animals.update_one(searchVal, {"$set": updateVal})                                          
            jsonVal = json_util.dumps((self.database.animals.find(searchVal, {"_id": False})))
            
            return jsonVal                                   
        else:
            raise e
            
            
    def delete(self, searchVal):
        """A method to delete data"""
        if searchVal:
            result = self.database.animals.delete_many(searchVal)
            jsonVal = json_util.dumps((self.database.animals.find(searchVal, {"_id": False})))
            
            return jsonVal
        else:
            raise Exception("Unable to delete, check the parameters and try again.")

