"""Store efficiently using pickle module. Module translates an in-memory Python object  
into a serialized byte stream—a string of bytes that can be written to any file-like object. 
"""

import pickle 

def storeData(): 
    # initializing data to be stored in db 
    TextDomain = {'key' : 'Text', 'name' : 'Text Analytics', 'confidence' : 90} 
    ImageDomain = {'key' : 'Image', 'name' : 'Image Analytics', 'confidence' : 90} 
    VisualDomain = {'key' : 'Visual', 'name' : 'Visualization', 'confidence' : 90} 

    # database 
    db = {} 
    db['domain1'] = TextDomain 
    db['domain2'] = ImageDomain 
    db['domain3'] = VisualDomain 

    # Its important to use binary mode 
    dbfile = open('tmp/dbfile_pickle.txt', 'wb') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 

def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('tmp/dbfile_pickle.txt', 'rb')      
    db = pickle.load(dbfile)
    for keys in db:
        print("keys: {}".format(db[keys])) 
    dbfile.close() 

if __name__ == '__main__': 
    storeData()
    loadData()