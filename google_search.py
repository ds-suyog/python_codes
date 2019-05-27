
try: 
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 
query = "python latest research papers"

#search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
for res in search(query, tld="com", num=10, stop=3, pause=2): 
    print(res) 

