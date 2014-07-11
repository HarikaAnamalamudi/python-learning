import urllib2
import urllib
import json

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
file = open("sample.html", "w")
file.write("<html><head>This is a sample output</head><body>\n")
file.write("<table>")
query = raw_input("What do you want to search for ? >> ")

query = urllib.urlencode( {'q' : query } )

response = urllib2.urlopen (url + query ).read()

data = json.loads ( response )

results = data [ 'responseData' ] [ 'results' ]

for result in results:
	file.write("<tr>")
        file.write("<td>")
	title = result['title']
        url = result['url']
        file.write(title)
	file.write("</td>")	
	file.write("<td>")
	file.write(url)
	file.write("</td>")
	file.write("</tr>")
file.write("</table>")
file.write("</body></html>")
