import requests
import urllib.request 
import json
import ssl 
import webbrowser 
ssl._create_default_https_context = ssl._create_unverified_context

f = open('helloworld.html','w')
message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()
webbrowser.open('file:///Library/Frameworks/Python.framework/Versions/3.8/bin/python-test/helloworld.html')


 url3 = 'http://127.0.0.1:8898/data' ,
            $.getJSON(url3,function(slots){
                console.log(slots),
            }); 