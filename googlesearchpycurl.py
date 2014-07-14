import pycurl
import urllib

with open('out.html', 'wb') as f:
    c = pycurl.Curl()
    url="http://google.com/search"
    query = raw_input("What do you want to search for ? >> ")
    query = urllib.urlencode( {'q' : query } )
    
    c.setopt(c.URL, url + '?' + query) 
    
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
