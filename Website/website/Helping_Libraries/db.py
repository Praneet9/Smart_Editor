from pymongo import MongoClient

def testingdb():
    print('Hello My DB')

# db = client.smart_editor
# nonfilled_collection = db.non_filled
# filled_collection = db.filled

def getConnection():
    client = MongoClient('localhost:27017')
    return client

def getDB(client):
    db = client.smart_editor
    return db

def getCollection(collection_name, db):
    collection = db[collection_name]
    return collection

def closeConnection(client):
    client.close()

##Database Helper functions
def insert_data(collection, args_dict):
    client = getConnection()
    db = getDB(client)
    collection_name = getCollection(collection, db)
    '''
    db_name -> string i.e name of the db
    args_dict -> a dictionary of entries in db
    '''
    collection_name.insert_one(args_dict)
    print('Data inserted successfully')
    closeConnection(client)

def read_data(collection):
    client = getConnection()
    db = getDB(client)
    collection_name = getCollection(collection, db)
    '''
    returns a cursor of objects
    which can be iterated and printed
    '''
    cols = collection_name.find({})
    closeConnection(client)
    return cols

#Update in data base
def update_data(collection, idno, updation):
    client = getConnection()
    db = getDB(client)
    collection_name = getCollection(collection, db)
    '''
    db_name -> string
    idno -> id number of database entry in dict
    eg:- {'id':'02'}
    updation -> dict of elements to be updated
    eg:-{
        '$set':{
            'name':'Kevin11',
            'contact':'9664820165'
        }
    }
    '''
    collection_name.update_one(idno, updation)
    closeConnection(client)
    print('Database updated successfully')

def delete_row(collection, idno):
    client = getConnection()
    db = getDB(client)
    collection_name = getCollection(collection, db)
    '''
    Deletes the complete row
    idno must be a dict {idno:'anything'}
    '''
    collection_name.delete_many(idno)
    closeConnection(client)
    print('Row deleted')
