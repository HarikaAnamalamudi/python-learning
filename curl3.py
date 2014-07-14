import pycurl

with open('out.html', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://google.com/search?#q=')
    query=raw_input("enter your search")
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
