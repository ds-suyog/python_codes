"""Store efficiently using pickle module. Module translates an in-memory Python object  
into a serialized byte stream—a string of bytes that can be written to any file-like object. 
"""

import pickle 

def storeData(): 
    # initializing data to be stored in db 
    TextDomain = {'key' : 'Text', 'name' : 'Text Analytics', 'confidence' : 90} 
    ImageDomain = {'key' : 'Image', 'name' : 'Image Analytics', 'confidence' : 80} 
  
    # database 
    db = {} 
    db['domain1'] = TextDomain 
    db['domain2'] = ImageDomain 
      
    # Its important to use binary mode 
    dbfile = open('tmp/storage_pickle.txt', 'wb') 
      
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
if __name__ == '__main__': 
    storeData() 