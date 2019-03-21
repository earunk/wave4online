from flask import Flask
# classes always start with capital

app = Flask(__name__)

# gives each file a unique name= __name__


@app.route('/')  # decorator 'http://www.google.com/'
def icehome():  # Home method
   """Icehome or Root Page."""
   return "<h1>Hello, Welcome to IceHouse</h1> <h3>Automation of Data\
Protection Operations and Management via RESTful APIs!</h3>"

app.run(port=2019)  # Specify a port number to listen
#adding an extra line to check if I am able to push this file to git
