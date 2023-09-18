from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<body>
<center>
<h1>CI/CD pipeline using GitHub Action </h1> <br>
<br>
<img src="https://raw.githubusercontent.com/aspdiscovery123/f1-application/main/edument-axoniq.webp?raw=true">
</center>
</body>
</html>
'''
